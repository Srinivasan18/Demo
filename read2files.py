#!/usr/bin/python
#Author of this script: Srinivasan Vasanth
#Date: Fri Jul 20 16:39:42 IST 2018
#Purpose of this script: Reading 2 files line by line
fname = input("Enter file name 1: ")
sname = input("Enter file name 2: ")
num_lines = 0
with open(fname, 'r') as f:
   for line in f:
       num_lines += 1
print("Number of lines:")
print(num_lines)
