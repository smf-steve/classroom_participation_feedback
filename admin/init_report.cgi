#! /bin/bash

## Simple script to create an report file, based upon information provided by the prof.

# Algorithm:
#   1. Source the environment
#      - Obtain date and time information
#      - Lookup Class information based upon WEEKDAY and Current Time
#      - define: CLASS, CLASS_DAYS, CLASS_WEEKDAY, CLASS_TIME, CLASS_24TIME
#      - determine not in session -- exit will occur
#
#   1. Validate Form Data  (note form uses lowercase, and env uses uppercase)
#      - Description
#      - Prompt
#      - Attendance
#
#   1. Log the information
#      logname: ../logs/admin.log
#
#   1. Return: main page

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

ADMIN_LOG_FILE=${LOGS}/admin/report_initialization.log
REPORT_FILE=${REPORTS}/$FULL_DATE:$CLASS-$CLASS_WEEKDAY-$CLASS_24TIME.env

# Extract values from the query string
if [[ -n "${QUERY_STRING}" ]] ; then 
    IFS="&" read -a pairs <<< "${QUERY_STRING}"
    for kp in "${pairs[@]}" ; do
      IFS="=" read var value <<< "${kp}"
      case "$var" in 
        description)
           DESCRIPTION="$( sed 's/+/ /g' <<< "$value" )"
           ;;
        prompt)
           PROMPT="$( sed 's/+/ /g' <<< "$value" )"
           ;;
        attendees)
           RECORDED_ATTENDEES="$value"
           ;;
      esac
    done   
fi

# If any of the values in the query string are empty then set to the defaults
[[ -z ${DESCRIPTION} ]]        && DESCRIPTION="${DEFAULT_DESCRIPTION}"
[[ -z ${PROMPT} ]]             && PROMPT="${DEFAULT_PROMPT}"
[[ -z ${RECORDED_ATTENDEES} ]] && RECORDED_ATTENDEES="${DEFAULT_RECORDED_ATTENDEES}"


# Create the log information
{ 
   echo -n ${FULL_DATE},${HOUR}:${MINUTE},${CLASS}-${CLASS_WEEKDAY}-$CLASS_24TIME,

   # If there is a Query String,
   # emit the "&" separated components onto a separate line.
   if [ -n "${QUERY_STRING}" ] ; then 
       IFS="&" read -a pairs <<< "${QUERY_STRING}"
       for kp in "${pairs[@]}" ; do
         echo -n "${kp},"
       done   
   fi
   echo
} | sed 's/,$//' >> $ADMIN_LOG_FILE


# Create/Recreate the initial report file
cat > ${REPORT_FILE} <<-EOF
# Prepared Date: $(date)

FILE_NAME="${FULL_DATE}:${CLASS}-${CLASS_WEEKDAY}-${CLASS_24TIME}.env"
CLASS="${CLASS}"
CLASS_WEEKDAY="${CLASS_WEEKDAY}"
CLASS_TIME="${CLASS_TIME}"
CLASS_24TIME="${CLASS_24TIME}"
CLASS_DATE="${FULL_DATE}"
DESCRIPTION="${DESCRIPTION}"
PROMPT="${PROMPT}"
RECORDED_ATTENDEES="${RECORDED_ATTENDEES}"
RATING_AVERAGE=0
RATING_MEDIAN=0
RATING_MODE=0
RATING_LOW=
RATING_HIGH=
RATINGS=()
NUM_RESPONDENTS=
RESPONSES=()
EOF

touch ${LOG_FILE}
${BIN}/log2report ${LOG_FILE}

cat <<-EOF
x-participation-info: ${CLASS} ${CLASS_WEEKDAY} ${CLASS_24TIME}
x-participation-date: $(date)
location: ./index.cgi

EOF

exit 0
