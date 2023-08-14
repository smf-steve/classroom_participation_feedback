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
      <title>Classroom Feedback</title>

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
        <li>COMP122     M/W         9:00<a href=""></a></li>
        <li>COMP122     T/R         9:00<a href=""></a></li>
        <li>COMP122L    M/W         10:30<a href=""></a></li>
        <li>COMP122L    T/R         12:30<a href=""></a></li>
        <li>COMP122L    T/R         10:30<a href=""></a></li>
      </ul>
      <a href="https://github.com/smf-steve/classroom_participation_feedback">Github: Classroom Participation and Feedback System</a></li>
      </ul>
    </div>
EOF

echo "<div class="container">"
  echo "<h5>Reports for Fall 2023 Classes</h5>"
  source ${BIN}/report2html
  report2html
echo "</div>"

cat <<EOF
</body>
</html>
EOF
