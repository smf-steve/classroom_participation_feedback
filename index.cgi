#! /bin/bash

source participation.env 
in_session_p
if [[ $? != 0 ]]  ; then
  : #exit 0;
fi


cat <<EOF

<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Participation and Feedback System</title>


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
      <h2>Participation and Feedback System</h2>
      Feel free to provided feedback to today's class.
   </div>
   <br>
   <div class="container" style="text-align: center;">
      <h3>$CLASS $CLASS_WEEKDAY @ $CLASS_TIME</h3>
      <a href=https://www.csun.edu/~steve/participation/input.cgi>
        <img  src="qr-code.png" style="margin-top: -14px;"
        alt="A QR code for https://www.csun.edu/~steve/participation/input.cgi">
      </a>
      <p>$(date)</p>
  </div>

</body>
</html>

EOF
