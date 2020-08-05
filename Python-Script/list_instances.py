import boto3
import sys
import os
mylist = []
#mylist = ['t2.small', 't2.small','t2.medium','t2.medium','t2.large']

if len(sys.argv) > 2:
    print ("usage: python list_instances.py 't2.medium'")
    sys.exit(1)

#region = os.environ.get('EC2REGION')

#if region is None:
#    print ("Please add a region or set the EC2REGION environment variable.")
#    sys.exit(1)
#region='us-east-2'
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    mylist.append(
            "{0}".format(instance.instance_type)
            )
if len(sys.argv) > 1:
    inst_type = sys.argv[1]
    for index, value in enumerate(mylist,start=1):
        if inst_type in value:
            print("Instance #{0}, {1}".format(index, value))
else:
    for index, value in enumerate(mylist,start=1):
        print("Instance #{0}, {1}".format(index, value))
