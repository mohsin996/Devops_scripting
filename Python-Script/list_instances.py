import boto3
import sys
import os
mylist = []

#Checking with the default list to test list operation
#mylist = ['t2.small', 't2.small','t2.medium','t2.medium','t2.large']

#check if more than 2 arguments passed
if len(sys.argv) > 2:
    print ("usage only with one argument: python list_instances.py 't2.medium'")
    sys.exit(1)

#Boto Script to fetch details about EC2 with default region configured with aws configure
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    mylist.append(
            "{0}".format(instance.instance_type)
            )
#condition based on the arguments passed
if len(sys.argv) > 1:
    inst_type = sys.argv[1]
    for index, value in enumerate(mylist,start=1):
        if inst_type in value:
            print("Instance #{0}, {1}".format(index, value))
else:
    for index, value in enumerate(mylist,start=1):
        print("Instance #{0}, {1}".format(index, value))
