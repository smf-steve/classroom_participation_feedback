#! /bin/bash

PARTICIPATION_HOME=".."
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
   <div>
      <h3>No class is currently in session</h3>
    </div>"
else
  source ${REPORT_FILE}
  PNG_FILE="qr-code.png"
  PNG_URL="../cgi/input.cgi"
  PNG_TITLE_DIV="
    <div>
      <h3>${CLASS} ${CLASS_WEEKDAY} @ ${CLASS_TIME}</h3>
      Feel free to provided feedback to today's class.
    </div>"
fi

cat <<EOF
content-type: text/html

<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta http-equiv="refresh" content="10">
      <title>Participation and Feedback</title>

      <!-- CSS CDN -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <link href="css/participation.css">

      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  </head>


<body class="text-bg-light p-3" id="body">
  
   <div class="container">
      <h2>Participation and Feedback</h2>
   </div>
   <br>
   <div class="container"  style="text-align: center;">
      ${PNG_TITLE_DIV}
      <a href="${PNG_URL}">
        <img  src="${PNG_FILE}" height="425" width="425"
        alt="A QR code to access the input.cgi script">
      </a>
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
    <input type="number" class="form-control" id="attendees_id" name="attendees"  value="${RECORDED_ATTENDEES}"/>
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

  # Process the current REPORT_FILE 
  # So that dynamic changes occur on the page
  echo "<div>"
    ${BIN}/report2html ${REPORT_FILE}
  echo "</div>"

fi

cat <<EOF
</body>
</html>

EOF



