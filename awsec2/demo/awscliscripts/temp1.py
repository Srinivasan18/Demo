while (reso == 'ec2' or reso == 'elb' or reso == 'rds' or reso == 'volume' or reso == 'snapshot' or reso == 'subnet' or reso == 'securitygroup'):
  if reso == image or reso == instance or reso == internet-gateway or reso == natgateway or reso == network-acl or reso == network-interface or reso == reserved-instances or reso == route-table or reso == security-group or reso == snapshot  or reso == subnet or reso == volume or reso == vpc or reso == vpc-peering-connection or reso == vpn-connection or reso == vpn-gateway:
     resdet = reso
  	 ec2amides = "ec2 describe-tags resource-id" + resid + "--filters Name=resource-id,Value=" + resid + "--region" + region
  	 awscmd2 = ec2amides
  	 awscmd1 = ec2ami
     print(awscmd1)
  elif resdet == reso == elb:
     elbdes = "elb describe-tags --load-balancer-name" + resid + "--region" + region
     awscmd2 = elbdes
  	 awscmd1 = elbs
     print(awscmd1)
   elif resdet == reso == rdss:
   	 rdsdes = "rds list-tags-for-resource --resource-name" + resid + "--region"
   	 awscmd2 = rdsdes
     awscmd1 = rdss
     print(awscmd1)
   elif resdet == reso == volumes:
     volumedes = "ec2 describe-tags resource-id" + resid + "--filters Name=resource-id,Value=" + resid + "--region"
   	 awscmd2 = volumedes
     awscmd1 = volumes
     print(awscmd1)
   elif resdet == reso == snapshots:
     snapdes = "ec2 describe-tags resource-id" + resid + "--filters Name=resource-id,Value=" + resid + "--region"
   	 awscmd2 = elbdes
     awscmd1 = snapshots
     print(awscmd1)
   elif resdet == reso == subnets:
   	 subdes = "ec2 describe-tags resource-id" + resid + "--filters Name=resource-id,Value=" + resid + "--region"
   	 awscmd2 = elbdes
     awscmd1 = subnets
     print(awscmd1)
   elif resdet == reso == securitygroups:
   	 secdes = 
   	awscmd2 = elbdes
     awscmd1 = securitygroup
     print(awscmd1)
   break