#! /bin/bash

export PARTICIPATION_HOME="."
source ${PARTICIPATION_HOME}/etc/participation.env 


LINK=
if [[ ${in_session} == "TRUE" ]]  ; then
  LINK="<li>Feedback Link for: <a href=\"./admin/index.cgi\">${CLASS} ${CLASS_WEEKDAY} ${CLASS_24TIME}</a></li>"
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
    <div class="container">
      <ul>
        ${LINK}
        <li><a href=""></a></li>
        <li><a href=""></a></li>
        <li><a href="https://github.com/smf-steve/classroom_participation_feedback">Github: Classroom Participation and Feedback System</a></li>
      </ul>
    </div>
EOF

source ${BIN}/report2html
report2html

cat <<EOF
</body>
</html>
EOF
