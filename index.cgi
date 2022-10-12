#! /bin/bash


source participation.env 

CLASS="COMP122"
CLASS_WEEKDAY=${WEEKDAY}
CLASS_TIME=$(class_time)

if [[ -z $CLASS_TIME ]] ; then
	# Class is not in session
	: #exit
fi

# Algorithm:
#   1. Source the environment
#      - Obtain date and time information
#   1. Lookup Class information based upon WEEKDAY and Current Time
#      - define: CLASS, CLASS_WEEKDAY, CLASS_TIME
#      - otherwise:  error page
#   
#   1. Present Form Date
#      - CSUN email address
#      - Participation Code
#      - Rating of the Day
#      - Feedback/response


cat <<EOF
x-participation: $CLASS $(date)
Content-Type: text/html

<!DOCTYPE html>
<html>
<body>

<h2>Participation System</h2>

<h3>$CLASS $CLASS_WEEKDAY @ $CLASS_TIME:00</h3>

<p>Today's Date: $(date)</p>

<p>
<form action="./participation_logger.cgi">
  <label for="email_id">CSUN Email Address:</label><br>
  <input type="email" id="email_id" name="email" 
         placeholder="@my.csun.edu" value=""><br>

  <label for="code_id">Participation Code:</label><br>
  <input type="text" id="code_id" name="code" value=""><br>

  <label for="rating_id">Value of Today's Class (0=low ... 10=high):</label><br>
  <input type="range" id="rating_id" name="rating" value="3" min="0" max="10"><br>

  <br><br>
  <label for="response_id">Feedback/Response:</label><br>
  <textarea id="response_id" name="response" rows="10" cols="80">
   Either provide feedback for today's class
   or Providy your response to prompt provided in class
  </textarea>


  <br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>
EOF

