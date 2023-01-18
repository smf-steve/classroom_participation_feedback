# Filters to handle a URL encoding from a POST to HTML symbols
#
# '+' -> ' '
s|+| |g

# remove the UTF-8 newlines 
s|%0D%0A| |g

# :name: ->  $(insert_image name)
s|%3A\([^%]*\)%3A|$(insert_image \1)|

# General handling of UTF+8 encodings
# - 4 byte sequence
s|%\(F.\)%\([89AB].\)%\([[89AB].\)%\([89AB].\)|$(utf8_2_html 0x\1 0x\2 0x\3 0x\4)|g
# - 3 byte sequence
s|%\(E.\)%\([89AB].\)%\([89AB].\)|$(utf8_2_html 0x\1 0x\2 0x\3)|g
# - 2 byte sequence
s|%\([CD].\)%\([89AB].\)|$(utf8_2_html 0x\1 0x\2)|g
# - 1 byte sequence
s|%\(..\)|$(utf8_2_html 0x\1)|g

# Remove leading whitespace and then blank lines
s|^[ \t]*||
/^$/d
