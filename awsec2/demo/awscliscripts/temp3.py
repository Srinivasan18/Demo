aws --profile agsafety ec2 describe-instances --filters 'Name=instance-idValues=+ + instid' --region eu-west-1
aws --profile agsafety ec2 create-tags --resources + instid --tags Key='Business Unit'Value=+ value1 Key='Environment'Value=+ value2 Key='Project'Value=+ value3 Key='Product'Value=+ value4 Key='Version'Value=+ value5 Key='Region'Value=+ value6 Key='Business_Model'Value=+ value7 Key='Service'Value=+ value8 Key='Customer'Value=+ value9 Key='Revenue_Type'Value=+ value10 Key='Requestor'Value=+ value11 Key='Provisioner'Value=+ value12 Key='Provisioner'Value=+ value13 Key='Ticket ID'Value=+ value14 Key='OS Version'Value=+ value15 Key='DB Version'Value=+ value16 Key='Retention Period'Value=+ value17 Key='Provisioning Month'Value=+ value18 --region eu-west-1

 "aws --profile agsafety ec2 create-tags --resources " + instid + " --tags Key='Business Unit',Value=" + value1 +  " Key='Environment',Value=" + value2 +  " Key='Project',Value=" + value3 + " Key='Product',Value=" + value4 + " Key='Version',Value=" + value5 + " Key='Region',Value=" + value6 + " Key='Business_Model',Value= "+ value7 + "Key='Service',Value=" + value8 + " Key='Customer',Value=" + value9 + " Key='Revenue_Type',Value=" + value10 + " Key='Requestor',Value=" + value11 + " Key='Provisioner',Value= " + value12 + " Key='Provisioner',Value= "+ value13 + " Key='Ticket ID',Value=" + value14 + " Key='OS Version',Value=" + value15 + " Key='DB Version',Value=" + value16 + " Key='Retention Period',Value=" + value17 + " Key='Provisioning Month',Value=" + value18 + " --region " + region

 " --tags Key='Business Unit',Value=" + value1 +  " Key='Environment',Value=" + value2 +  " Key='Project',Value=" + value3 + " Key='Product',Value=" + value4 + " Key='Version',Value=" + value5 + " Key='Region',Value=" + value6 + " Key='Business_Model',Value= "+ value7 + "Key='Service',Value=" + value8 + " Key='Customer',Value=" + value9 + " Key='Revenue_Type',Value=" + value10 + " Key='Requestor',Value=" + value11 + " Key='Provisioner',Value= " + value12 + " Key='Provisioner',Value= "+ value13 + " Key='Ticket ID',Value=" + value14 + " Key='OS Version',Value=" + value15 + " Key='DB Version',Value=" + value16 + " Key='Retention Period',Value=" + value17 + " Key='Provisioning Month',Value=" + value18 + " --region " + region
 
value1 = str(input("value - Business Unit: "))
value2 = str(input("value - Environment: "))
value3 = str(input("value - Project: "))
value4 = str(input("value - Name: "))
value5 = str(input("value - Product: "))
value6 = str(input("value - Version: "))
value7 = str(input("value - Region: "))
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

 elb describe-tags --load-balancer-name --region + region

 elb add-tags --load-balancer-name + resid + " --tags Key='Business Unit',Value=" + value1 +  " Key='Environment',Value=" + value2 +  " Key='Project',Value=" + value3 + " Key='Name',Value=" + value4 + " Key='Region',Value=" + value7 + " Key='Business_Model',Value= "+ value8 + "Key='Service',Value=" + value9 + " Key='Customer',Value=" + value10 + " Key='Revenue_Type',Value=" + value11 + " Key='Requestor',Value=" + value12 + " Key='Provisioner',Value= " + value13 + " Key='Ticket ID',Value=" + value14 + " Key='Retention Period',Value=" + value17 + " Key='Provisioning Month',Value=" + value18 + " --region " + region


image 
instance 
internet-gateway 
launch-template
natgateway  
network-acl 
network-interface
reserved-instances 
route-table  
security-group  
snapshot
spot-instances-request 
subnet 
volume
vpc  
vpc-peering-connection
vpn-connection 
vpn-gateway 