cmd2 = "ec2 create-tags --resources " + instid + " --tags Key='Business Unit',Value=" + value1 +  " Key=Environment,Value=" + value2  +  " Key=Project,Value=" + value3 + " Key=Product,Value=" + value4 + " Key=Version,Value=" + value5 + " Key=Region,Value=" + value6 + " Key=Business_Model,Value= "+ value7 + " --region "


print("Choose resource type: ec2 elb rds ami volume snapshot subnet securitygroup")
restype = str(input("AWS resourcetype: "))
#instid = str(input("Instance ID: "))
resdet = open("resource.txt")

cmd2 = "ec2 create-tags --resources " + instid + " --tags Key='Business Unit',Value=" + value1 +  " Key=Environment,Value=" + value2  +  " Key=Project,Value=" + value3 + " Key=Name,Value=" + value4 + " Key=Product,Value=" + value5 + " Key=Version,Value=" + value6 + " Key=Region,Value= " + value7 + + "Key='Business_Model',Value=" + value8 + " Key='Service',Value=" + value9 + " Key='Customer',Value=" + value10 + " Key='Revenue_Type',Value=" + value11 + " Key='Requestor',Value=" + value12 + " Key='Provisioner',Value="+ value13 + " Key='Ticket ID',Value=" + value14 + " Key='OS Version',Value=" + value15 + " Key='DB Version',Value=" + value16 + " Key='Retention Period',Value=" + value17 + " Key='Provisioning Month',Value=" + value18 + " --region "
Choose resource type: ec2 elb rds ami volume snapshot subnet securitygroup


while (reso == 'ec2' or reso == 'elb' or reso == 'rds' or reso == 'volume' or reso == 'snapshot' or reso == 'subnet' or reso == 'securitygroup'):
  if resdet == reso == 'ec2':
     awscmd1 = ec2ami
     print(awscmd1)
  elif resdet == reso == elb:
  	 elbdes = elb describe-tags --load-balancer-name + reso + "--region" + region
  	 awscmd1 = elb
     print(awscmd1)
   elif resdet == reso == rds
     awscmd1 = rds
     print(awscmd1)
   elif resdet == reso == volume
     awscmd1 = volume
     print(awscmd1)
   elif resdet == reso == snapshot
     awscmd1 = snapshot
     print(awscmd1)
   elif resdet == reso == subnet
     awscmd1 = subnet
     print(awscmd1)
   elif resdet == reso == securitygroup
     awscmd1 = securitygroup
     print(awscmd1)
   break


ec2ami = "ec2 describe-instances --filters Name=instance-id,Values=" + instid + " --region "
elbs =
rdss = 
volumes =
snapshots =
subnet =
securitygroup =