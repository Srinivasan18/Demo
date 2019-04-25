#!/bin/bash

read -p "Enter imgid : " imgid
read -p "Enter region : " region
aws --profile agsafety ec2  describe-images --image-ids $imgid --region $region  | grep -w "DeviceName\|VolumeSize"  | awk '{print $4}'

#read -p "Enter keyname : " keyname
#read -p "Enter subnet : " subnet
#read -p "Enter sgroup : " sgroup
#read -p "Enter count : " count
#read -p "Enter instype : " instype
#read -p "Enter privip : " privip
#read -p "Enter instname : " instname
#read -p "Enter regionname : " regionname
#read -p "Enter region : " region
read -p "Do you want to assign private IP (y/n)? " CONT
   echo
   if [ "$CONT" = "y" ]; then
   read -p "Enter privip : " privip
   fi
echo "privateip = --private-ip-address $privip"
#echo "aws --profile agsafety ec2 run-instances --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --private-ip-address $privip --disable-api-termination --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=TRAINING},{Key=Name,Value=$instname},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2}]' --region $region"
####################################################################################################################################	
#echo "aws --profile agsafety ec2 run-instances --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=TRAINING},{Key=Name,Value=$instname},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2}]' --region $region"

echo "#############################################################################################################################"
#aws ec2 run-instances  --iam-instance-profile Name=CloudWatchrole --image-id ami-28e07e50  --count 1 --instance-type t2.micro --key-name agLSMVJNJ_TRN --security-group-ids sg-0c2db4c5cbb0cb5c2 --vpc-id vpc-1c0ff364 --subnet-id subnet-7002773b  --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg}]' 'ResourceType=instance,Tags=[{Key=Business Unit,Value=agSafety}]' 'ResourceType=instance,Tags=[{Key=Business_Modle,Value=Single Tenant}]' 'ResourceType=instance,Tags=[{Key=Customer,Value=JNJ}]' 'ResourceType=instance,Tags=[{Key=Environment,Value=TRAINING}]' 'ResourceType=instance,Tags=[{Key=Name,Value=Test}]' 'ResourceType=instance,Tags=[{Key=Product,Value=Arisg}]' 'ResourceType=instance,Tags=[{Key=Region,Value=Oregon}]' 'ResourceType=instance,Tags=[{Key=Service,Value=EC2}]'--region us-west-2

echo "#############################################################################################################################"

echo "aws --profile agsafety ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role --image-id $imgid --block-device-mappings file://blockdev.json --user-data file://my_script.txt --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=TRAINING},{Key=Name,Value=$instname},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2}]' --region $region"
