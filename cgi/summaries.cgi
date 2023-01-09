#! /bin/bash

PARTICIPATION_HOME=".."
source ${PARTICIPATION_HOME}/etc/participation.env 

cat <<EOF
content-type: text/html

<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Participation and Feedback</title>

      <!-- CSS CDN -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <link href="css/participation.css">

      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  </head>


<body class="text-bg-light p-3" id="body">

EOF

# Process any log reports from the last two sessions
#  -- this should be done in a better way, but good enough for now.
#
# This approach, as opposed to a simple `ls`, is required because of the
# execution speed of the `ls` command.  This is related to how CSUN's
# web infrastructure works either because of security concerns or 
# a misconfigured filesystem.  

X=( ${LOGS}/*.log )                 # run `ls` command
for (( i=0; i< ${#X[@]} ; i++ )) ; do
  echo ${X[$i]}
done | sort -nr | sed -n '1,2p' |
  while read _log ; do
     ${BIN}/log2report ${_log}
  done
${BIN}/report2html

cat <<EOF
</body>
</html>

EOF
