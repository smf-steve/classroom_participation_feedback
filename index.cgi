#! /bin/bash

export PARTICIPATION_HOME="."
source ${PARTICIPATION_HOME}/etc/participation.env 


INSESSON=
if [[ ${in_session} == "TRUE" ]]  ; then
  INSESSION="<div class=container>
    <h5>Current class in session: <a href=\"./admin/index.cgi\">${CLASS} ${CLASS_WEEKDAY} ${CLASS_TIME}</a></h5>
    </div>
    <p>"
fi

echo
cat <<EOF
<!DOCTYPE html>
<html lang="en">
  <head>
      <title>Classroom Feedback for Fall 2024</title>

      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- CSS CDN -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <link rel="stylesheet" href="css/participation.css">

      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  </head>


  <body class="text-bg-light p-3" id="body">
  
    <div class="container">
      <h2>Classroom Feedback</h2>
    </div>
    ${INSESSION}
    <div class="container">
      <h5>Classes Associated with the Classroom Feedback System</h5>
      <ul>
        <li>COMP122     M/W         10:00<a href=""></a></li>
        <li>COMP122     T/R         10:00<a href=""></a></li>
        <li>COMP122L    M/W         11:30<a href=""></a></li>
        <li>COMP122L    T/R          1:30<a href=""></a></li>
        <li>COMP122L    T/R         11:30<a href=""></a></li>
      </ul>
      <a href="https://github.com/smf-steve/classroom_participation_feedback">Github: Classroom Participation and Feedback System</a>
      Previous Reports:
        <ul>
         <li><a href="../feedback_s23"> Spring 2023</a></li>
         <li><a href="../feedback_f23"> Fall 2023  </a></li>
         <li><a href="../feedback_f22"> Fall 2022  </a></li>
        </ul>
      </ul>
    </div>
EOF

echo "<div class="container">"
  echo "<h5>Reports for Fall 2024 Classes</h5>"
  source ${BIN}/report2html
  report2html
echo "</div>"

cat <<EOF
</body>
</html>
EOF
