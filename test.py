#!/usr/bin/python
#Author of this script: Srinivasan Vasanth
#Date: Mon Jan 15 12:52:03 IST 2018
#Purpose of this script: test
#Author of this script: Srinivasan Vasanth
#Date: Thu Jul 12 15:58:48 IST 2018
#Purpose of this script: testing menuscript
# Version 1
## Show menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')
 
## Get input ###
choice = raw_input('Enter your choice [1-3] : ')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Starting backup...")
elif choice == 2:
        print ("Starting user management...")
elif choice == 3:
        print ("Rebooting the server...")
else:    ## default ##
        print ("Invalid number. Try again...")

