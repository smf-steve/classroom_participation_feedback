#! /bin/bash

## Simple script to log Participation
## These are the students that participated in class.

# participation_log.cgi
# Algorithm:
#   1. validate in class time
#      - add an exception by a code
#   1. determine parameters
#   1. validate form info
#      - CSUN email address
#      - Participation Code
#      - text box for feedback/response

#   1. log information

source participation.env


# Emit body


DATE=$(date)
WEEKDAY=$(date +%A )
DAY=$(date +%d )
MONTH=$(date +%m )
HOUR=$(date +%H )
MINUTE=$(date +%M )

echo -n $MONTH/$DAY,$HOUR:$MINUTE,

# If there is a Query String,
# emit the "&" separated components onto a separate line.
if [ -n "${QUERY_STRING}" ] ; then 
    IFS="&" read -a pairs <<< "${QUERY_STRING}"
    for kp in "${pairs[@]}" ; do
      echo -n "${kp},"
    done   
fi
echo

9 - 10:45
2 - 3:45

if [[ $HOUR > 12 ]] ; then 
   # Afternoon class
   $(( CLASS = CLASS ))
else
   # Morning class
fi
LOG_FILE="$MONTH:$DAY:$WEEKDAY:"


echo $MONTH/$DAY,$HOUR:$MINUTE,


# Provide a response

# Emit response headers
echo "X-function: Echoing Request"
echo "Content-type: text/plain"
echo "Location: https://www.csun.edu/~steve/participation/recorded.html"

# Emit blank line
echo ""

exit 0
