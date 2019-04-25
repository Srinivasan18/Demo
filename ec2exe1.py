#!/usr/bin/python
#Author of this script: Srinivasan Vasanth
#Date: Tue Oct  9 15:59:57 IST 2018
#Purpose of this script: awscli EC2 execution
import urllib3
urllib3.disable_warnings()
import os
import subprocess
from subprocess import call
import awscli
--image-id $imgid
--instance-type $instid
--key-name $keyname
--security-group-ids <value>
--subnet-id <value>
#--user-data <value>
--enable-api-termination
--ebs-optimized
--private-ip-address <value>
--tag-specifications <value>
--count <value>
#--associate-public-ip-address | --no-associate-public-ip-address

