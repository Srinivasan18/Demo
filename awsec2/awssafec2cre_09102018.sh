#!/bin/bash

read -p "Enter imgid : " imgid
read -p "Enter keyname : " keyname
read -p "Enter subnet : " subnet
read -p "Enter sgroup : " sgroup
read -p "Enter count : " count
read -p "Enter instype : " instype
read -p "Enter privip : " privip
read -p "Enter instname : " instname
read -p "Enter regionname : " regionname
read -p "Enter region : " region


echo "aws --profile agsafety ec2 run-instances --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --private-ip-address $privip --disable-api-termination --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=TRAINING},{Key=Name,Value=$instname},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2}]' --region $region"
####################################################################################################################################
#echo "aws --profile agsafety ec2 run-instances --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --disable-api-termination --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=TRAINING},{Key=Name,Value=$instname},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2}]' --region $region"

echo "#############################################################################################################################"
