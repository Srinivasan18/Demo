#!/bin/bash

read -p "Enter cidr_range : " cidr
read -p "Enter region : " region
read -p "Enter key1 : " key1
read -p "Enter value1 : " value1
read -p "Enter key1 : " key2
read -p "Enter value1 : " value2
read -p "Enter key1 : " key3
read -p "Enter value1 : " value3
read -p "Enter key1 : " key4
read -p "Enter value1 : " value4
read -p "Enter key1 : " key5
read -p "Enter value1 : " value5
read -p "Enter key1 : " key6
read -p "Enter value1 : " value6


awssrini ec2 create-vpc --cidr-block 10.120.0.0/16 'ResourceType=vpc,Tags=[{Key=Project,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=DEV},{Key=Product,Value=Arisg},{Key=Region,Value=$regionname},{Key=Service,Value=EC2},{Key=Requestor,Value=vasanth},{Key=Revenue_Type,Value=non-revenue},{Key=Business_Model,Value=private},{Key=Ticket_ID,Value=private},{Key=Retention_Period,Value=1month},{Key=Provisioning_Month,Value=November},{Key=Service,Value=VPC}]' --region eu-west-1 --dry-run 