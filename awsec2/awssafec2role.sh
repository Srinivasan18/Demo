#!/bin/bash

read -p "Enter instid : " instid

echo " aws ec2 associate-iam-instance-profile --instance-id $instId --iam-instance-profile Name=CLoudWatch_Role"
