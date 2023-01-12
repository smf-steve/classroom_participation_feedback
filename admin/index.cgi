#! /bin/bash

export PARTICIPATION_HOME=".."
source ${PARTICIPATION_HOME}/etc/participation.env 

## If class is in session, then it should build the default
## .env file.
##
## either via the submit
## or by using the defaults -- which should be provided via participation.env


if [[ ${in_session} == "FALSE" ]] ; then
  PNG_FILE="not-in-session.png"
  PNG_URL="../not-in-session.html"
  PNG_TITLE_DIV="
   <div class="container">
      <h2>No class is currently in session</h2>
    </div>"
else
  PNG_FILE="qr-code.png"
  PNG_URL="../cgi/input.cgi"
  PNG_TITLE_DIV="
    <div class="container">
      <h2>${CLASS}</h2>
      $(date "+%A @ ${CLASS_TIME}, %b %d, %Y")
      <br>
      Feel free to provided feedback to today's class.
    </div>"
fi

cat <<EOF
content-type: text/html

<!DOCTYPE html>
<html lang="en">
  <head>
      <title>Feedback Link</title>

      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta http-equiv="refresh" content="10">


      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <link rel="stylesheet" href="../css/participation.css?nocache=$$">

      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  </head>

<body class="text-bg-light p-3" id="body" onload="scrollToBottom()">

    ${PNG_TITLE_DIV}

    <div class="container">
    <div class="row">
      <div class="col">
        <a href="${PNG_URL}">
          <img src="${PNG_FILE}" height="450px" width="450px"
          alt="A QR code to access the input.cgi script">
        </a>
      </div>
EOF


if [[ ${in_session} == "TRUE" ]] ; then
  # Process the current REPORT_FILE 
  # So that dynamic changes occur on the page
  source ${BIN}/report2html
  source ${REPORT_FILE}

  echo '<div class="col">'
    present_response
  echo '</div>'
  echo '<div class="col">'
    present_chart
  echo '</div>'
fi
cat <<EOF
  </div>
EOF




if [[ ${in_session} == "TRUE" ]] ; then
  cat <<EOF
<form action="./init_report.cgi">
  <div class="container">
    <label for="description_id" class="form-label">Class Coverage:</label>
    <textarea class="form-control" id="description_id" rows="3" cols="80" name="description" placeholder="${DESCRIPTION}"></textarea>
  </div>
  <div class="container">
    <label for="prompt_id" class="form-label">Prompt:</label>
    <textarea class="form-control" id="prompt_id" rows="1" cols="80" name="prompt" placeholder="${PROMPT}"></textarea>
  </div>
  <div class="container">
    <label for="attendees_id" class="form-label" id="attendees">Number of Attendees</label>
    <input type="number" class="form-control" id="attendees_id" name="attendees"  placeholder="${RECORDED_ATTENDEES}"/>
  </div>
  <!-- Submit buttons -->
  <div class="container">
    <button type="submit" id="dark" class="btn btn-outline-dark" value="Submit">Submit</button>
  </div>
  <div class="container">
    <button type="submit" id="light" class="visually-hidden" value="Submit">Submit</button>
  </div>
</form>
EOF

fi

cat <<EOF
    <script>
      element = document.getElementById("txt_box_1");

      function scrollToBottom() {
        element.scrollIntoView(false);
      }
    </script>
</body>
</html>

EOF



