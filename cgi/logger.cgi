#! /bin/bash

## Simple script to log participation

# Algorithm:
#   1. Source the environment
#      - Obtain date and time information
#      - Lookup Class information based upon WEEKDAY and Current Time
#      - define: CLASS, CLASS_DAYS, CLASS_WEEKDAY, CLASS_TIME, CLASS_24TIME
#      - determine not in session -- exit will occur
#
#   1. Validate Form Data
#      - CSUN email address
#      - Rating of the Day
#      - Feedback/response
#
#   1. Log the information
#      logname: logs/$CLASS-$CLASS_WEEKDAY-$CLASS_24TIME:$MONTH-$DAY
#
#   1. Update the report file
#
#   1. Return Thank you page

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

# Create the log information
LOG_LINE=$( 
{ 
  echo -n ${FULL_DATE},${HOUR}:${MINUTE},${CLASS}-${CLASS_WEEKDAY}-${CLASS_24TIME},

  # If there is a Query String,
  # emit the "&" separated components onto a separate line.
  if [ -n "${QUERY_STRING}" ] ; then 
      IFS="&" read -a pairs <<< "${QUERY_STRING}"
      for kp in "${pairs[@]}" ; do
        echo -n "${kp},"
      done   
  fi
  echo
} | sed 's/,$//' )



# Check to see if there is a dup
grep  ${LOG_LINE} ${LOG_FILE}
if [[ $? == 1 ]] ; then
  # There were no dups so add it to the logfile
  flock -x local-lock-file -c "echo ${LOG_LINE} >>${LOG_FILE}"
  ${BIN}/log2report ${LOG_FILE}
fi


cat <<-EOF
x-participation-info: ${CLASS} ${CLASS_WEEKDAY} ${CLASS_24TIME}
x-participation-date: $(date)
location: ./class_responses.cgi

EOF

exit 0
