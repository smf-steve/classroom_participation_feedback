#! /bin/bash

source participation.env 
in_session_p
if [[ $? != 0 ]]  ; then
  in_session=FALSE
fi

if [[ $in_session == "FALSE" ]] ; then
  PNG_FILE="not-in-session.png"
else
  PNG_FILE="qr-code.png"
  PNG_TITLE_DIV="
    <div>
      <h3>$CLASS $CLASS_WEEKDAY @ $CLASS_TIME</h3>
      Feel free to provided feedback to today's class.
    </div>"

fi

cat <<EOF

<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Classroom Participation and Feedback System</title>


      <!-- CSS CDN -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">

      <style>
        .container textarea{
          resize: none;
          font-family: sans-serif;
        }
        .container{
          font-family: sans-serif;
          margin-bottom: 1.2em;
        }
        h2{
          margin-top: 1%;
        }
        #rating_id{
          width: 50%;
        }
        #sun{
          margin-left: 85%;
          background-color: transparent;
          background-repeat: no-repeat;
          border: none;
          outline: none;
        }
        #moon{
          margin-left: 85%;
          background-color: transparent;
          background-repeat: no-repeat;
          border: none;
          outline: none;
        }
        #sun:hover{
          background-color: gray;
        }
        #moon:hover{
          background-color: #777;
        }
        .form-label{
          display: block;
        }
      </style>
  </head>


<body class="text-bg-light p-3" id="body">
  
   <div class="container">
      <h2>Classroom Participation and Feedback System</h2>
   </div>
   <br>
   <div class="container"  style="text-align: center;">
      ${PNG_TITLE_DIV}
      <a href=https://www.csun.edu/~steve/participation/input.cgi>
        <img  src="${PNG_FILE}" height="425" width="425"
        alt="A QR code to access the input.cgi script">
      </a>
  </div>
EOF

# Process any log reports from the last two sessions
#  -- this should be done in a better way, but good enough for now.
#
# This is approach as opposed to a simple `ls` was required because
# of the way CSUN's infrastructure works either because of security concerns
# or a misconfigured filesystem.
X=( $(echo logs/*.log) ) 
for (( i=0; i< ${#X[@]} ; i++ )) ; do
  echo ${X[$i]}
done  | sort -nr | head -2 |
  while read _log ; do
     ./log2report  ${_log}
  done
./report2html

cat <<EOF
</body>
</html>

EOF



