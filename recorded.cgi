#! /bin/bash

source participation.env 
in_session_p
if [[ $? != 0 ]]  ; then
  cat <<EOF
x-participation-info: No class in session
x-participation-date: $(date)
location: ./not-in-session.html

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
        <meta http-equiv="Cache-Control" content="no-cache, no-store,     must-revalidate">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Expires" content="0">
        <meta http-equiv="refresh" content="10">
        <meta charset="utf-8">
        <title>Class Feedback</title>

        <!-- CSS CDN -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

    </head>
<body class="text-bg-light p-3" id="body">

   <div class="container">
      <h2>${CLASS} ${CLASS_WEEKDAY} ${CLASS_TIME}</h2>
   </div>
   <br>
   <div class="container">
      Your feedback has been included in the information below.
   </div>  
   <br><br>

EOF

# If this program is called in the proper order, then both the LOG_FILE and REPORT_FILE should exist.
[ ! -f  ${LOG_FILE} ] && exit 1
[ ! -f ${REPORT_FILE} ] && exit 1

./log2report ${LOG_FILE}
./report2html ${REPORT_FILE}

cat <<EOF
</body>
</html>
EOF