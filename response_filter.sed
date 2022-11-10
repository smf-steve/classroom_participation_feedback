# remove the response= tag and any whitespace
# Line 9, prior to this, we need to identify which should not be transformd to \&x
#   or perhaps, based up the size of the resulting number, pt it back into %format
#   s|\&#F\(.....\);|UTF-8: 0xF\1|
s/^response= *//
s/+/ /g
s/%0D%0A/ /g
s|%3A\(party_parrot\)%3A|<img hieght=\'36px\' alt=\'emoji: \1\' loading=\'lazy\' src=\'images/\1.gif\'>|
s/%\([0-9A-F][0-9A-F]\)/\&#x\1;/g
s/^ *//
/^$/d

