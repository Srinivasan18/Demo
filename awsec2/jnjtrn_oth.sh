

aws --profile agsafety ec2 run-instances --image-id ami-0e5fc65ff41cc6273  --count 1 --instance-type m5.xlarge --key-name agLSMVJNJ_TRN --security-group-ids sg-0c2db4c5cbb0cb5c2 --subnet-id subnet-7002773b --disable-api-termination --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=TRAINING},{Key=Name,Value=agLSMV_JnJ_TRN_CCM_1A},{Key=Product,Value=Arisg},{Key=Region,Value=Oregon},{Key=Service,Value=EC2}]' --region us-west-2


echo "#############################################################################################################################"
aws --profile agsafety ec2 run-instances --image-id ami-0a993615e7589f469  --count 1 --instance-type m5.xlarge --key-name agLSMVJNJ_TRN --security-group-ids sg-0c2db4c5cbb0cb5c2 --subnet-id subnet-7002773b --disable-api-termination --tag-specifications 'ResourceType=instance,Tags=[{Key=Application,Value=ARISg},{Key=Business Unit,Value=agSafety},{Key=Business_Modle,Value=Single Tenant},{Key=Customer,Value=JNJ},{Key=Environment,Value=TRAINING},{Key=Name,Value=agLSMV_JnJ_TRN_NT_Services_1A},{Key=Product,Value=Arisg},{Key=Region,Value=Oregon},{Key=Service,Value=EC2}]' --region us-west-2



