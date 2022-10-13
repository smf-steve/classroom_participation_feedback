#! /bin/bash

# Algorithm:
#   1. Source the environment
#      - Obtain date and time information
#      - Lookup Class information based upon WEEKDAY and Current Time
#      - define: CLASS, CLASS_WEEKDAY, CLASS_TIME
#      - determine not in session -- exit will occur
#
#   1. Present Form Data
#      - CSUN email address
#      - Participation Code
#      - Rating of the Day
#      - Feedback/response

source participation.env 
# Note: program my exit as appropriate in participation.env


cat <<EOF
x-program: participation
x-program-info: $CLASS $CLASS_WEEKDAY $CLASS_TIME
x-program-date: $(date)
content-Type: text/html

<!DOCTYPE html>
<html>
<body>

<h2>Participation System</h2>

<h3>$CLASS $CLASS_WEEKDAY @ $CLASS_TIME</h3>

<p>Today's Date: $(date)</p>

<p>
<form action="./logger.cgi">
  <label for="email_id">CSUN Email Address:</label><br>
  <input type="email" id="email_id" name="email" 
         placeholder="@my.csun.edu" value=""><br>

  <label for="code_id">Participation Code:</label><br>
  <input type="text" id="code_id" name="code" value=""><br>

  <label for="rating_id">Value of Today's Class (0=low ... 10=high):</label><br>
  <input type="range" id="rating_id" name="rating" min="0" max="10"><br>

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

