#!/bin/bash


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


echo "aws elb create-load-balancer --load-balancer-name my-load-balancer --listeners "Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80" --subnets subnet-15aaab61 --security-groups sg-a61988c3"


