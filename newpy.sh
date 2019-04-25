#!/bin/bash
#cd /root/scripts/
read -p "Enter pyfile : " pyfile
read -p "Author:" author
read -p "Reviewer:" review 
read -p "Purpose:" purpose
echo "#!/usr/bin/python" >> $pyfile.py
echo "#Purpose of this script: $purpose" >> $pyfile.py
echo "#Date: $(date)" >> $pyfile.py
echo "#Author of this script: $author" >> $pyfile.py
echo "#Reviewer of this script: $review" >> $pyfile.py
chmod +x $pyfile.py
vi $pyfile.py
