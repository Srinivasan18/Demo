#!/bin/bash
#cd /root/scripts/
read -p "Enter bashfile : " shfile
read -p "Author:" author
read -p "Reviewer:" review 
read -p "Purpose:" purpose
echo "#!/usr/bin/bash" >> $shfile.sh
echo "#Purpose of this script: $purpose" >> $shfile.sh
echo "#Date: $(date)" >> $shfile.sh
echo "#Author of this script: $author" >> $shfile.sh
echo "#Reviewer of this script: $review" >> $shfile.sh
chmod +x $shfile.sh
vi $shfile.sh
