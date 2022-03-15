#!/bin/bash
############################
# My Twitter @MahmoudZ0x1
# My LinkedIn https://www.linkedin.com/in/mahmoud-mahfouz-29b80a1b1/
# special thanks to @Limbo0x01

# sub_index is a simple bash script
# used to gather the sub-domains
# from the target main website page

# usage : ./sub_index.sh domain.com
############################
if [ $# != 1 ]
then
echo "Usage : $0 domain.com"
exit 0
fi
############################
echo "[*] Start"
echo "[*] Target is $1"
file1=$1.txt
wget $1 -O $file1 -o tmp.txt
############################
cat $file1 | grep "href=\|src=" | grep "http" | grep "//" | cut -d "\"" -f 2 | cut -d "/" -f 3 | grep "\." | grep $(echo $1 | cut -d '.' -f 1) | grep -v "www.$1" | uniq > sub.txt
############################
for x in $(cat sub.txt)
do
if [[ $(ping -c 1 -w 2 $x) ]]
then echo "[+]" $x " >> " $(host -t A $x | grep "has address" | cut -d ' ' -f 4) | tee -a results.txt
fi
done
rm $file1 sub.txt tmp.txt
echo "[*]"
echo "[*] Done"
############################
