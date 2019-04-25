#!/bin/bash

#Purpose of this script: To deploy AWS EC2 using CLI
#Date: Mon Nov 19 14:27:57 IST 2018
#Author of this script: Srinivasan Vasanth
#Reviewer of this script: Manish Kumar

read -p "Enter imgid : " imgid
read -p "Enter region : " region
#aws --profile agsafety ec2  describe-images --image-ids $imgid --region $region  | grep -w "DeviceName\|VolumeSize\|SnapshotId"  
read -p "Enter keyname : " keyname
read -p "Enter subnet : " subnet
read -p "Enter sgroup : " sgroup
read -p "Enter count : " count
read -p "Enter instype : " instype
read -p "Enter instname : " instname
read -p "Enter regionname : " regionname
read -p "Key1 : " key1
read -p "Value1 : " value1
read -p "Key2 : " key2
read -p "Value2 : " value2
read -p "Key3 : " key3
read -p "Value3 : " value3
read -p "Key4 : " key4
read -p "Value4 : " value4
read -p "Key5 : " key5
read -p "Value5 : " value5
read -p "Key6 : " key6
read -p "Value6 : " value6
read -p "Key7 : " key7
read -p "Value7 : " value7
read -p "Key8 : " key8
read -p "Value8 : " value8
read -p "Private IP if required (y/n)? " CONT
   echo
   if [ "$CONT" = "y" ]; then
    read -p "Enter private ip : " privip
    echo "aws ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role  --user-data file://my_script.txt  --private-ip-address $privip --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=$key1,Value=$value1},{Key=$key2,Value=$value2},{Key=$key3,Value=$value3},{Key=$key4,Value=$value4},{Key=$key5,Value=$value5},{Key=Name,Value=$instname},{Key=$key6,Value=$value6},{Key=$key7,Value=$value7},{Key=$key8,Value=$value8}]' --region $region";
    else
    echo "aws ec2 run-instances --iam-instance-profile Name=CLoudWatch_Role  --user-data file://my_script.txt  --image-id $imgid  --count $count --instance-type $instype --key-name $keyname --security-group-ids $sgroup --subnet-id $subnet --disable-api-termination  --tag-specifications 'ResourceType=instance,Tags=[{Key=$key1,Value=$value1},{Key=$key2,Value=$value2},{Key=$key3,Value=$value3},{Key=$key4,Value=$value4},{Key=$key5,Value=$value5},{Key=Name,Value=$instname},{Key=$key6,Value=$value6},{Key=$key7,Value=$value7},{Key=$key8,Value=$value8}]' --region $region";
   fi







