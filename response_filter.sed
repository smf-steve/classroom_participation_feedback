# remove the response= tag and any whitespace
s/^response= *//
s/+/ /g
s/%0D%0A/ /g
s|%3A\(party_parrot\)%3A|<img alt=\"emoji: \1\" loading=\"lazy\" src=\"images/\1.gif\">|
s/%\([0-9A-F][0-9A-F]\)/\&#x\1;/g
s/^ *//
/^$/d

