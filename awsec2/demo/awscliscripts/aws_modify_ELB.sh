#!/bin/bash

read -p "Enter AWS Account : " accid
read -p "Enter imgid : " imgid
read -p "Enter region : " region
aws --profile agsafety ec2  describe-images --image-ids $imgid --region $region  | grep -w "DeviceName\|VolumeSize\|SnapshotId"  
read -p "Enter keyname : " keyname
read -p "Enter subnet : " subnet
read -p "Enter sgroup : " sgroup
read -p "Enter count : " count
read -p "Enter instype : " instype
read -p "Enter privip : " privip
read -p "Enter instname : " instname
read -p "Enter regionname : " regionname
#read -p "Enter region : " region
#read -p "Do you want to assign private IP (y/n)? " CONT
   echo
   if [ "$CONT" = "y" ]; then
   read -p "Enter privip : " privip
   fi
#echo "privateip = --private-ip-address $privip"


#echo "aws --profile agsafety ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role --block-device-mappings file://blockdev.json --user-data file://my_script.txt  --private-ip-address $privip  --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=DEV},{Key=Name,Value=$instname},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2}]' --region $region"



echo "aws --profile agsafety ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role --block-device-mappings file://blockdev.json --user-data file://my_script.txt  --private-ip-address $privip  --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=DEV},{Key=Name,Value=$instname},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2}]' --region $region"



