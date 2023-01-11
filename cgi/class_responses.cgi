#! /bin/bash
PARTICIPATION_HOME=".."
source ${PARTICIPATION_HOME}/etc/participation.env 

if [[ ${in_session} == "FALSE" ]]  ; then
  cat <<EOF
x-participation-info: No class in session
x-participation-date: $(date)
location: ../not-in-session.html

EOF
  exit 0;
fi



cat <<EOF
x-participation-info: ${CLASS} ${CLASS_WEEKDAY} ${CLASS_24TIME}
x-participation-date: $(date)
content-Type: text/html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="10">

    <title>Today's Feedback</title>
    <!-- CSS CDN -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <link rel="stylesheet" href="../css/participation.css">

    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

  </head>
  <body class="text-bg-light p-3"  id="body" onload="scrollToBottom()">
    <div class="container">
      <h2>${CLASS}</h2>
      <h4>${CLASS_WEEKDAY} @ ${CLASS_TIME}</h4>
      $(date "+%b %d, %Y")
    </div>

EOF


source ${BIN}/report2html
source ${REPORT_FILE}

cat <<EOF
    <div class="container">
    <div comment="header">
        <span> Class Coverage: ${DESCRIPTION}</span>
        <span style="float:right">Respondents: ${NUM_RESPONDENTS}/${RECORDED_ATTENDEES}</span>
    </div>
EOF

    present_text_box

cat <<EOF
    </div>
    <script>
      element = document.getElementById("txt_box_1");

      function scrollToBottom() {
        element.scrollIntoView(false);
      }
    </script>
  </body>
</html>
EOF