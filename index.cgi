#! /bin/bash

source participation.env 
in_session_p
if [[ $? != 0 ]]  ; then
  : #exit 0;
fi


cat <<EOF

<!DOCTYPE html>
<html>
<body>

<h2>$CLASS Participation and Feedback System</h2>

Welcome to the $CLASS Participation and Feedback System.  Via this tool, you will be able to provide Professor Fitzgerald with feedback associate with our class today.  



br><br><br><br><br><br><br><br><br>
<div style="text-align: center;">
<h3>$CLASS $CLASS_WEEKDAY @ $CLASS_TIME</h3>

  <p>Use your phone to scan the QR code, or click on the QR code.
  <br>
  <a href=https://www.csun.edu/~steve/participation/input.cgi>
     <img  src="qr-code.png"
      alt="A QR code for https://www.csun.edu/~steve/participation/input.cgi">
  </a>
  <p>Today's Date: $(date)</p>
  <br>
</div>

</body>
</html>

EOF
