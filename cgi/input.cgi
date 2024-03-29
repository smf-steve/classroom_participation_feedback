#! /bin/bash

# Algorithm:
#   1. Source the environment
#      - Obtain date and time information
#      - Lookup Class information based upon WEEKDAY and Current Time
#      - define: CLASS, CLASS_DAYS, CLASS_WEEKDAY, CLASS_TIME, CLASS_24TIME
#      - determine not in session -- exit will occur
#
#   1. Present Form Data
#      - CSUN email address
#      - Rating of the Day
#      - Feedback/response

export PARTICIPATION_HOME=".."
source ${PARTICIPATION_HOME}/etc/participation.env 

if [[ ${in_session} == "FALSE" ]]  ; then
  cat <<EOF
x-participation-info: No class in session
x-participation-date: $(date)
location: ../not-in-session.html

EOF
  exit 0;
fi

if [[ -f ${REPORT_FILE} ]] ; then
  source ${REPORT_FILE}
fi
cat <<EOF
x-participation-info: ${CLASS} ${CLASS_WEEKDAY} ${CLASS_24TIME}
x-participation-date: $(date)
content-Type: text/html

<!DOCTYPE html>
<html lang="en">
  <head>
      <title>Feedback Input</title>

      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <link rel="stylesheet" href="../css/participation.css?nocache=$$">
  </head>

  <body class="text-bg-light p-3" id="body">
    <!-- Sun -->
      <button type="button" id="sun" class="btn" onclick="contrastDark()">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-sun" viewBox="0 0 16 16">
        <path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"/>
      </svg>
    </button>
    
    <!-- Crescent moon -->
    <button type="button" id="moon" class="visually-hidden" onclick="contrastLight()";>
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-moon" viewBox="0 0 16 16">
        <path d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278zM4.858 1.311A7.269 7.269 0 0 0 1.025 7.71c0 4.02 3.279 7.276 7.319 7.276a7.316 7.316 0 0 0 5.205-2.162c-.337.042-.68.063-1.029.063-4.61 0-8.343-3.714-8.343-8.29 0-1.167.242-2.278.681-3.286z"/>
      </svg>
    </button>

    <!-- Top of Page -->
    <div class="container">
      <h2>${CLASS}</h2>
      $(date "+%A @ ${CLASS_TIME}, %b %d, %Y")
    </div>

    <div class="container">
      <label for="response_id" class="form-label">Class Coverage:</label>
      <textarea class="form-control" id="response_id" cols="80" name="response" readonly> ${DESCRIPTION}</textarea>
    </div>
    <div class="container">
    <hr style="margin-bottom: 20px">
    </div>


    <form action="./logger.cgi">

      <!-- Feedback text area with label -->
      <div class="container">
          <label for="response_id" class="form-label">Prompt: ${PROMPT}</label>
          <textarea class="form-control" id="response_id" rows="6" cols="80" name="response" placeholder=
          "Enter your response here!"></textarea>
      </div>

      <!-- Range slider with label -->
      <div class="container">
          <label for="rating_id" class="form-label">Overall Rating (0=low &rarr; 10=high):</label>
          <input type="range" class="form-label" id="rating_id" name="rating" min="-0.5" value="-0.5" max="10" step="0.5"/></span>
      </div>

      <!-- Email box with label -->
      <div class="container">
          <label for="email_id" class="form-label" id="email">CSUN Email Address:</label>
          <input type="email" autocomplete="on" class="form-control" id="email_id" name="email" placeholder="@my.csun.edu" value=""/>
      </div>

      <!-- Submit buttons -->
      <br>
      <div class="container">
        <button type="submit" id="dark" class="btn btn-outline-dark" value="Submit">Submit</button>
      </div>
      <div class="container">
        <button type="submit" id="light" class="visually-hidden" value="Submit">Submit</button>
      </div>
    </form>

      <script async>
      function contrastDark(){
        document.getElementById('body').className='text-bg-dark p-3';
        document.getElementById('sun').className='visually-hidden'; 
        document.getElementById('moon').className='btn btn-outline-light';
        document.getElementById('dark').className='visually-hidden';
        document.getElementById('light').className='btn btn-outline-light';
      }
      function contrastLight(){
        document.getElementById('body').className = 'text-bg-light p-3';
        document.getElementById('sun').className='btn';
        document.getElementById('moon').className='visually-hidden';  
        document.getElementById('dark').className='btn btn-outline-dark';
        document.getElementById('light').className='visually-hidden';     
      }
     </script>
  </body>
</html>
EOF

