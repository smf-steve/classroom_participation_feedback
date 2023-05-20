# ! /bin/bash

# Responses_per_student

cat ../logs/*.log | grep "%40my.csun.edu" |\
  awk -F, '{ print $1, $6}'               |\
  sed -e 's/email=//' -e 's/%40/@/'       |\
  sort -n -f                               \
  > master.log

awk '{ print $2}' master.log             |\
  sort -f | uniq -ci                      \
  > count.log

awk '{print $2}' count.log > user.list


cat user.list | while read _user ; do
  grep "$_user" master.log   |\
  tail -1 > $_user.log
done
