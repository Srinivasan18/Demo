#!/usr/bin/python
#Author of this script: Srinivasan Vasanth
#Date: Thu Jul 12 16:02:57 IST 2018
#Purpose of this script: execute regular aws cli commands
import urllib3
urllib3.disable_warnings()
import os
import subprocess
from subprocess import call
import awscli
if hasattr(__builtins__, 'raw_input'):
      input=raw_input
list=['agmaster', 'agbalance', 'agqnc', 'agsafety', 'agregulatory', 'agclinical']
print ("Type the account")
acc = str(input("AWS account: "))
awsbal='aws --profile agbalance '
awssaf='aws --profile agsafety '
awsmas='aws --profile agmaster '
awscln='aws --profile agclinical '
awsreg='aws --profile agregulatory '
awsqnc='aws --profile agqnc '
awssrini='aws --profile srinivav'
region='aws ec2 describe-regions --region eu-west-1 --profile agqnc'
while (acc == 'agmaster' or acc == 'agbalance' or acc == 'agqnc' or acc == 'agsafety' or acc == 'agregulatory' or acc == 'agclinical'):
  if acc == 'agmaster':
    subprocess.call(region, shell=True)
    print (30 * '-')     
    agmas = input("Command or ctr+z :>  ")
    command = awsmas + agmas
    print (command)
    subprocess.call(command, shell=True, executable='/bin/bash')
    print (30 * '-')

  elif acc == 'agbalance':
   subprocess.call(region, shell=True)
   print (30 * '-')
   agbal = input("Command or ctr+z :>  ") 
   command = awsbal + agbal
   print (command)
   subprocess.call(command, shell=True, executable='/bin/bash')

  elif acc == 'agqnc':
   subprocess.call(region, shell=True)
   print (30 * '-')
   agqnc = input("Command or ctr+z :>  ")
   command = awsqnc + agqnc
   print (command)
   subprocess.call(command, shell=True, executable='/bin/bash')

  elif acc == 'agsafety':
   subprocess.call(region, shell=True)
   print (30 * '-')
   agsaf = input("Command or ctr+z :>  ")                         
   command = awssaf + agsaf
   print (command)
   subprocess.call(command, shell=True, executable='/bin/bash')

  elif acc == 'agregulatory':
   subprocess.call(region, shell=True)
   print (30 * '-')
   agreg = input("Command or ctr+z :>  ")                          
   command = awsreg + agreg
   print (command)
   subprocess.call(command, shell=True, executable='/bin/bash')

  elif acc == 'agclinical':
   subprocess.call(region, shell=True)
   print (30 * '-')
   agcln = input("Command or ctr+z :>  ")                            
   command = awscln + agcln
   print (command)
   subprocess.call(command, shell=True, executable='/bin/bash')
  
 elif acc == 'srinivas':
   subprocess.call(region, shell=True)
   print (30 * '-')
   
   agsri = input("Command or ctr+z :>  ")                            
   command = awssrini + agsri
   print (command)
   subprocess.call(command, shell=True, executable='/bin/bash')
  else: 
    print("Try again with correct accout name")
