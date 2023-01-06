#! /bin/bash

source participation.env 
in_session_p
if [[ $? != 0 ]]  ; then
  in_session=FALSE
fi

## If class is in session, then it should build the default
## .env file.
##
## either via the submit
## or by using the defaults -- which should be provided via participation.env


if [[ $in_session == "FALSE" ]] ; then
  PNG_FILE="images/not-in-session.png"
else
  PNG_FILE="images/qr-code.png"
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
      <a href=input.cgi>
        <img  src="${PNG_FILE}" height="425" width="425"
        alt="A QR code to access the input.cgi script">
      </a>
  </div>
<form action="./init_report.cgi">
  <div class="container">
    <label for="description_id" class="form-label">Class Description:</label>
    <textarea class="form-control" id="description_id" rows="3" cols="80" name="description" placeholder="${DESCRIPTION}"></textarea>
  </div>
  <div class="container">
    <label for="prompt_id" class="form-label">Prompt:</label>
    <textarea class="form-control" id="prompt_id" rows="1" cols="80" name="prompt" placeholder="${PROMPT}"></textarea>
  </div>
  <div class="container">
    <label for="attendees_id" class="form-label" id="attendees">Number of Attendees</label>
    <input type="number" class="form-control" id="attendees_id" name="attendees"  value=""/>
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

# Process any log reports from the last two sessions
#  -- this should be done in a better way, but good enough for now.
#
# This approach, as opposed to a simple `ls`, is required because of the
# execution speed of the `ls` command.  This is related to how CSUN's
# web infrastructure works either because of security concerns or 
# a misconfigured filesystem.  

X=( $(echo logs/*.log) )                 # run `ls` command
for (( i=0; i< ${#X[@]} ; i++ )) ; do
  echo ${X[$i]}
done | sort -nr | sed -n '1,2p' |
  while read _log ; do
     ./log2report  ${_log}
  done
./report2html

cat <<EOF
</body>
</html>

EOF



