# remove the response= tag and any whitespace
s/^response= *//
s/+/ /g
s/%0D%0A/ /g
s/%2C/\&#x2C;/g
s/%\([0-9A-F][0-9A-F]\)/\&#x\1;/g
s/^ *//
/^$/d

