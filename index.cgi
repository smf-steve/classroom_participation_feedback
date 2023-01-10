#! /bin/bash

export PARTICIPATION_HOME="."
source ${PARTICIPATION_HOME}/etc/participation.env 


REFRESH=
if [[ ${in_session} == "TRUE" ]]  ; then
  REFRESH='<meta http-equiv="refresh" content="10">'
fi

echo
cat <<EOF
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      ${REFRESH}
      <title>Participation and Feedback</title>

      <!-- CSS CDN -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <link href="css/participation.css">

      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  </head>


  <body class="text-bg-light p-3" id="body">
  
    <div class="container">
      <h2>Participation and Feedback</h2>
    </div>
    <br>
    <ul>
      <li><a href="./admin/index.cgi"> Initialize Current Class</a></li>
    </ul>
EOF

${BIN}/report2html

cat <<EOF
</body>
</html>
EOF
