#!/bin/bash

echo "############################################"
echo "ec2 describe-instances --filter Name=tag,Values=SIT --region us-west-2"
echo "ec2 describe-instances --instance-ids i-083c824b2478069b3 --region us-west-2"
echo "ec2 describe-instances --filter Name=ip-address,Values=10.116.5.74 --region us-west-2"

cat /root/awsregions


read -p "Enter aws command : " awscommand
for i in `aws --profile agsafety ec2 describe-regions --output text --region eu-west-1| cut -f3`; do \
aws --profile agsafety $awscommand --region $i --output table; 
aws --profile agbalance $awscommand --region $i --output table; 
aws --profile agclinical $awscommand --region $i --output table; 
aws --profile agregulatory $awscommand --region $i --output table; 
aws --profile agqnc $awscommand --region $i --output table; 
done



