#! /bin/bash

## Simple script to log participation

# Algorithm:
#   1. Source the environment
#      - Obtain date and time information
#      - Lookup Class information based upon WEEKDAY and Current Time
#      - define: CLASS, CLASS_WEEKDAY, CLASS_TIME
#      - determine not in session -- exit will occur
#
#   1. Validate Form Data
#      - CSUN email address
#      - Rating of the Day
#      - Feedback/response
#
#   1. Log the information
#      logname: logs/$CLASS-$CLASS_WEEKDAY-$CLASS_TIME:$MONTH-$DAY
#
#   1. Return Thank you page

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

LOG_FILE=logs/$FULL_DATE:$CLASS-$CLASS_WEEKDAY-$CLASS_TIME.log


# Create the log information
{ 
   echo -n $FULL_DATE,$HOUR:$MINUTE,$CLASS-$CLASS_WEEKDAY-$CLASS_TIME,

   # If there is a Query String,
   # emit the "&" separated components onto a separate line.
   if [ -n "${QUERY_STRING}" ] ; then 
       IFS="&" read -a pairs <<< "${QUERY_STRING}"
       for kp in "${pairs[@]}" ; do
         echo -n "${kp},"
       done   
   fi
   echo
} | sed 's/,$//' >> $LOG_FILE

cat <<-EOF
x-participation-info: $CLASS $CLASS_WEEKDAY $CLASS_TIME
x-participation-date: $(date)
location: ./recorded.html

EOF

exit 0
