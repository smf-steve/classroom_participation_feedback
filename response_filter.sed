# remove the response= tag and any whitespace
s/^response= *//
s/+/ /g
s/%0D%0A/ /g
s/^ *//
/^$/d

