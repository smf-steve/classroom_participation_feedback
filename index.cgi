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

<h2>COMP122 Participation and Feedback System</h2>

<p><span id=current_date>Current Date/Time</span></p>
  <script>
    document.getElementById("current_date").innerHTML = Date();
  </script>
</html>


Welcome to the COMP122 Participation and Feedback System.  Via this tool, you will be able to provide Professor Fitzgerald with feedback associate with our class today.  

<br><br><br><br><br><br><br><br><br>
<div style="text-align: center;">
  <p>Use your phone to scan the QR code, or click on the QR code.
  <br>
  <a href=https://www.csun.edu/~steve/participation/input.cgi>
     <img  src="qr-code.png"
      alt="A QR code for https://www.csun.edu/~steve/participation/input.cgi">
  </a>
  <br>
  <a href=https://www.csun.edu/~steve/participation/input.cgi>
    <small>https://www.csun.edu/~steve/participation/input.cgi</small>
  </a>

</div>

</body>
</html>

EOF
