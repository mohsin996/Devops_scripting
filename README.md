# Devops_scripting

This repositpory contains Python script to list EC2 instances with boto3  and Ansible Script to provision EC2 instance

## Cloning the repository
```bash
$ git clone https://github.com/mohsin996/Devops_scripting.git
Cloning into 'Devops_scripting'...
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 23 (delta 3), reused 9 (delta 0), pack-reused 0
Unpacking objects: 100% (23/23), done.
$ cd Devops_scripting/
```
## Pre Environment setup

- Python3 & pip3 is pre-installed
- Creating IAM user in AWS with access keys details programmatic user with access keys to configure aws-cli.
- Creatig IAM role "myFirstEC2role" thats has *AmazonEC2ReadOnlyAccess* policy attached, which we will assign it to EC2 instance to acquire temporary credentials so that boto/aws-cli can fetch results.

#### Installing awscli ansible boto boto3 with pip
```bash
$ python --version
Python 3.8.0
$ pip install awscli ansible boto boto3
```
#### configuring aws-cli 
```bash
$ aws configure
AWS Access Key ID [******************XX]:
AWS Secret Access Key [*****************XX]:
Default region name [us-east-2]:
Default output format [table]:
```
### Running python script list_instances.py.
#### without Parameters
```bash
$ cd Python-Script/
$ python list_instances.py
Instance #1, t2.small
Instance #2, t2.small
Instance #3, t2.medium
Instance #4, t2.medium
Instance #5, t2.large
```
#### with Parameters
```
$ python list_instances.py 't2.medium'
Instance #3, t2.medium
Instance #4, t2.medium
```
## Provisioning EC2 instance by Ansible playbook

### Making Ansible ready to work with AWS APIs
```bash
$ ansible --version
ansible 2.9.11
```
Creating config key file and directory structure
```bash
 $ ssh-keygen -t rsa -b 4096 -f ~/.ssh/my_aws
 $ cd ../Ansible-playbook/
 $ mkdir -p group_vars/all/
```
Creating a ansible-vault to store AWS keys, this is same user we used before in running script locally
```bash
 $ ansible-vault create group_vars/all/awspass.yml
 New Vault password:
 Confirm New Vault password:
```
vault should have two key enteries `ec2_access_key` & `ec2_secret_key`
```
$ ansible-vault edit group_vars/all/awspass.yml
ec2_access_key: ******************
ec2_secret_key: **************************
```
Ansible Directory Structure will look like
```
├── Ansible-playbook
│   ├── ansible.cfg
│   ├── group_vars
│   │   └── all
│   │       └── awspass.yml
│   └── playbook.yml
```
```bash
$ cat ansible.cfg
[defaults]
host_key_checking = False
private_key_file = ~/.ssh/my_aws
```
### Running the playbook now 
```
$ ansible-playbook playbook.yml --ask-vault-pass
```
```bash
PLAY RECAP ***************************************************************************
50.18.240.116              : ok=3    changed=2
localhost                  : ok=6    changed=1
```
Copying the script to EC2 server ( replace the dns hostname of your ec2 server)
```bash
scp -p -i ~/.ssh/my_aws list_instances.py ec2-user@ec2-50-18-240-116.us-west-1.compute.amazonaws.com:
```
### Running the python script in EC2 instance
Note: we are using python3 in ec2 instance
```bash

$ ssh ec2-user@ec2-50-18-240-116.us-west-1.compute.amazonaws.com -i ~/.ssh/my_aws

Last login: Wed Aug  5 04:48:02 2020 from 
       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|
https://aws.amazon.com/amazon-linux-2/

[ec2-user@ip-172-31-9-11 ~]$ python3 list_instances.py
Instance #1, t2.micro
```
# License
[Apache]
