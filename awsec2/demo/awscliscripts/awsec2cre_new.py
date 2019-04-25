#!/usr/bin/python
#Author of this script: Srinivasan Vasanth
#Date: Thu Jul 12 16:02:57 IST 2018
#Purpose of this script: execute regular aws cli commands
import urllib3
urllib3.disable_warnings()
import os
import subprocess
from subprocess import call
import awscli
if hasattr(__builtins__, 'raw_input'):
      input=raw_input

acc = str(input("AWS account: "))
instid = str(input("Instance ID: "))
region = str(input("region: "))
cmd1 = "ec2 describe-instances --filters "Name=instance-id,Values=%instid" --region %region"
cmd2 = 'aws --profile agsafety ec2 create-tags --resources %instid --tags Key='Business Unit',Value=%value1 Key='Environment',Value=%value2 Key='Project',Value=%value3 Key='Product',Value=%value4 Key='Version',Value=%value5 Key='Region',Value=%value6 Key='Business_Model',Value=%value7 Key='Service',Value=%value8 Key='Customer',Value=%value9 Key='Revenue_Type',Value=%value10 Key='Requestor',Value=%value11 Key='Provisioner',Value=%value12 Key='Provisioner',Value=%value13 Key='Ticket ID',Value=%value14 Key='OS Version',Value=%value15 Key='DB Version',Value=%value16 Key='Retention Period',Value=%value17 Key='Provisioning Month',Value=%value18 --region eu-west-1'
Value1 = str(input("Value : "))
Value2 = str(input("Value : "))
Value3 = str(input("Value : "))
Value4 = str(input("Value : "))
Value5 = str(input("Value : "))
Value6 = str(input("Value : "))
Value7 = str(input("Value : "))
Value8 = str(input("Value : "))
Value9 = str(input("Value : "))
Value10 = str(input("Value : "))
Value11 = str(input("Value : "))
Value12 = str(input("Value : "))
Value13 = str(input("Value : "))
Value14 = str(input("Value : "))
Value15 = str(input("Value : "))
Value16 = str(input("Value : "))
Value17 = str(input("Value : "))
Value18 = str(input("Value : "))

awsbal='aws --profile agbalance '
awssaf='aws --profile agsafety '
awsmas='aws --profile agmaster '
awscln='aws --profile agclinical '
awsreg='aws --profile agregulatory '
awsqnc='aws --profile agqnc '


####################################################
###Instance tag modification#####
while (acc == 'agmaster' or acc == 'agbalance' or acc == 'agqnc' or acc == 'agsafety' or acc == 'agregulatory' or acc == 'agclinical'):
  if acc == 'agsafety':
     awscmd = awssaf + cmd1
	 print (awscmd)
	 awstagch = awssaf + cmd2 
	 print (awstagch)
  elif acc == 'agbalance':
  	 awscmd = awsbal + cmd1
	 print (awscmd)
	 awstagch = awsbal + cmd2 
	 print (awstagch)
  elif acc == 'agmaster':
  	 awscmd = awsmas + cmd1
	 print (awscmd)
	 awstagch = awsmas + cmd2 
	 print (awstagch)
  elif acc == 'agqnc':
  	 awscmd = awsqnc + cmd1
	 print (awscmd)
	 awstagch = awsqnc + cmd2 
	 print (awstagch)
  elif acc == 'agregulatory':
  	 awscmd = awsreg + cmd1
	 print (awscmd)
	 awstagch = awsreg + cmd2 
	 print (awstagch)
  elif acc == 'agclinical':
  	 awscmd = awscln + cmd1
	 print (awscmd)
	 awstagch = awscln + cmd2 
	 print (awstagch)
  break




	






