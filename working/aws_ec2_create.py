#!/usr/bin/python
#Purpose of this script: AWS_Ec2_create
#Date: Tue Nov 20 12:48:29 IST 2018
#Author of this script: Srinivasan_Vasanth
#Reviewer of this script: Manish_Kumar
#!/usr/bin/python
#Purpose of this script: AWS EC2 instance tagging accross all Accounts
#Date: Thu Nov 15 13:25:37 IST 2018
#Author of this script: Srinivasan Vasanth
#Reviewer of this script: Manish Kumar

import urllib3
urllib3.disable_warnings()
import os
import subprocess
from subprocess import call
import awscli
if hasattr(__builtins__, 'raw_input'):
      input=raw_input

acc = str(input("AWS account: "))
imgid = str(input("image ID: "))
region = str(input("region ID: "))
keyname = str(input("keyname: "))
subnet = str(input("subnet ID: "))
sgroup = str(input("security_group ID: "))
count = str(input("Count: "))
instype = str(input("insttype: "))
value1 = str(input("value - Business Unit: "))
value2 = str(input("value - Environment: "))
value3 = str(input("value - Project: "))
value4 = str(input("value - Name: "))
value5 = str(input("value - Product: "))
value6 = str(input("value - Version: "))
value7 = str(input("value - Region Name: "))
value8 = str(input("value - Business_Model: "))
value9 = str(input("value - Service: "))
value10 = str(input("value - Customer: "))
value11 = str(input("value - Revenue_Type: "))
value12 = str(input("value - Requestor: "))
value13 = str(input("value - Provisioner: "))
value14 = str(input("value - Ticket ID: "))
value15 = str(input("value - OS Version: "))
value16 = str(input("value - DB Version: "))
value17 = str(input("value - Retention Period: "))
value18 = str(input("value - Provisioning Month: "))
print("Do you have reserved private IP address, Type yes/no?")
answer = input()
if 'yes':
	cmd2 = "ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role  --user-data file://my_script.txt   --image-id " + imgid +  " --count " + count + " --instance-type " + instype + " --key-name " + keyname + " --security-group-ids " + sgroup + " --subnet-id " + subnet + " --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=Business Unit,Value=" + value1 + "}," +  " {Key=Environment,Value=" + value2 + "},"  +  " {Key=Project,Value=" + value3 + "}," + " {Key=Name,Value=" + value4 + "}," + " {Key=Product,Value=" + value5 + "}," + " {Key=Version,Value=" + value6 + "}," + " {Key=Region,Value=" + value7 + "}," + "{Key='Business_Model',Value=" + value8 + "}," + " {Key='Service',Value=" + value9 + "}," + " {Key='Customer',Value=" + value10 + "}," + " {Key='Revenue_Type',Value=" + value11 + "}," + " {Key='Requestor',Value=" + value12 + "}," + " {Key='Provisioner',Value="+ value13 + "}," + " {Key=Ticket ID,Value=" + value14 + "}," + " {Key=OS Version,Value=" + value15 + "}," + " {Key=DB Version,Value=" + value16 + "}," + " {Key=Retention Period,Value=" + value17 + "}," + " {Key=Provisioning Month,Value=" + value18 + "}]'" + " --region "
elif 'no':
	cmd2 = "ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role  --user-data file://my_script.txt  --private-ip-address " + privip + " --image-id " + imgid +  " --count " + count + " --instance-type " + instype + " --key-name " + keyname + " --security-group-ids " + sgroup + " --subnet-id " + subnet + " --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=Business Unit,Value=" + value1 + "}," +  " {Key=Environment,Value=" + value2 + "},"  +  " {Key=Project,Value=" + value3 + "}," + " {Key=Name,Value=" + value4 + "}," + " {Key=Product,Value=" + value5 + "}," + " {Key=Version,Value=" + value6 + "}," + " {Key=Region,Value=" + value7 + "}," + "{Key='Business_Model',Value=" + value8 + "}," + " {Key='Service',Value=" + value9 + "}," + " {Key='Customer',Value=" + value10 + "}," + " {Key='Revenue_Type',Value=" + value11 + "}," + " {Key='Requestor',Value=" + value12 + "}," + " {Key='Provisioner',Value="+ value13 + "}," + " {Key=Ticket ID,Value=" + value14 + "}," + " {Key=OS Version,Value=" + value15 + "}," + " {Key=DB Version,Value=" + value16 + "}," + " {Key=Retention Period,Value=" + value17 + "}," + " {Key=Provisioning Month,Value=" + value18 + "}]'" + " --region "
	break    
#cmd2 = "ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role  --user-data file://my_script.txt  + --image-id" + imgid +  "--count" + count + "--instance-type" + instype + "--key-name" + keyname + "--security-group-ids" + sgroup + "--subnet-id" + subnet + "--disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key='Business Unit',Value=" + value1 + "}," +  " {Key=Environment,Value=" + value2 + "},"  +  " {Key=Project,Value=" + value3 + "}," + " {Key=Name,Value=" + value4 + "}," + " {Key=Product,Value=" + value5 + "}," + " {Key=Version,Value=" + value6 + "}," + " {Key=Region,Value=" + value7 + "}," + "{Key='Business_Model',Value=" + value8 + "}," + " {Key='Service',Value=" + value9 + "}," + " {Key='Customer',Value=" + value10 + "}," + " {Key='Revenue_Type',Value=" + value11 + "}," + " {Key='Requestor',Value=" + value12 + "}," + " {Key='Provisioner',Value="+ value13 + "}," + " {Key='Ticket ID',Value=" + value14 + "}," + " {Key='OS Version',Value=" + value15 + "}," + " {Key='DB Version',Value=" + value16 + "}," + " {Key='Retention Period',Value=" + value17 + "}," + " {Key='Provisioning Month',Value=" + value18 + "}]'" + " --region "
#cmd3 = "ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role  --user-data file://my_script.txt  --private-ip-address" + privip + "--image-id" + imgid +  "--count" + count + "--instance-type" + instype + "--key-name" + keyname + "--security-group-ids" + sgroup + "--subnet-id" + subnet + "--disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key='Business Unit',Value=" + value1 + "}," +  " {Key=Environment,Value=" + value2 + "},"  +  " {Key=Project,Value=" + value3 + "}," + " {Key=Name,Value=" + value4 + "}," + " {Key=Product,Value=" + value5 + "}," + " {Key=Version,Value=" + value6 + "}," + " {Key=Region,Value=" + value7 + "}," + "{Key='Business_Model',Value=" + value8 + "}," + " {Key='Service',Value=" + value9 + "}," + " {Key='Customer',Value=" + value10 + "}," + " {Key='Revenue_Type',Value=" + value11 + "}," + " {Key='Requestor',Value=" + value12 + "}," + " {Key='Provisioner',Value="+ value13 + "}," + " {Key='Ticket ID',Value=" + value14 + "}," + " {Key='OS Version',Value=" + value15 + "}," + " {Key='DB Version',Value=" + value16 + "}," + " {Key='Retention Period',Value=" + value17 + "}," + " {Key='Provisioning Month',Value=" + value18 + "}]'" + " --region "
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
     awstagch = awssaf + cmd2 + region
     print(awstagch)
  elif acc == 'agbalance':
	 awstagch = awsbal + cmd2 + region 
	 print(awstagch)
  elif acc == 'agmaster':
	 awstagch = awsmas + cmd2 + region
	 print(awstagch)
  elif acc == 'agqnc':
	 awstagch = awsqnc + cmd2 + region 
	 print(awstagch)
  elif acc == 'agregulatory':
	 awstagch = awsreg + cmd2 + region 
	 print(awstagch)
  elif acc == 'agclinical':
	 awstagch = awscln + cmd2 + region 
	 print(awstagch)
  break
print("####################################################################")
print("Verify above deployment configuration, Type yes/no?")
print("####################################################################")
answer = input()
if 'yes':
	subprocess.call(awstagch, shell=True, executable='/bin/bash')
elif 'no':
	print("Correct the configuration and execute again !")
	break    




	







