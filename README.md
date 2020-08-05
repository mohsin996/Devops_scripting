# Devops_scripting

This repositpory contains Ad-hoc Python and Ansible Scripts

## Installations for Locally running Python script
Pre Assumption 
- Python3 & pip3 is pre-installed
- [IAM](https://console.aws.amazon.com/iam/home?region=us-east-2#/users) user in AWS with access keys details programmatic user with access keys to configure aws-cli.
- Default AWS region is hard coded as `us-east-2`, can be made user input value later
```bash
$ python --version
Python 3.8.0
$ pip install awscli ansible boto boto3
```
#### aws-cli configurations.
```bash
$ aws configure
AWS Access Key ID [******************XX]:
AWS Secret Access Key [*****************XX]:
Default region name [us-east-2]:
Default output format [table]:
```
#### Running script list_instances.py.
```bash
$ python list_instances.py
Instance #1, t2.small
Instance #2, t2.small
Instance #3, t2.medium
Instance #4, t2.medium
Instance #5, t2.large
```
```
$ python list_instances.py 't2.medium'
Instance #3, t2.medium
Instance #4, t2.medium
```
## Provisioning EC2 instance by Ansible playbook

Pre-Assumption:- Working Ansible setup
```bash
$ ansible --version
ansible 2.9.11
```
Creating config file, keys and directory structure
```bash
 $ ssh-keygen -t rsa -b 4096 -f ~/.ssh/my_aws
 $ mkdir -p Ansible-playbook/group_vars/all/
 $ cd Ansible-playbook/
 $ touch playbook.yml
```
Give login password to vault 
```bash
 $ ansible-vault create group_vars/all/awspass.yml
 New Vault password:
 Confirm New Vault password:
```
Copy the keys in the vault file 
```
$ ansible-vault edit group_vars/all/awspass.yml
ec2_access_key: ******************
ec2_secret_key: **************************
```
Directory Structure
```
├── Ansible-playbook
│   ├── ansible.cfg
│   ├── group_vars
│   │   └── all
│   │       └── awspass.yml
│   └── playbook.yml
```
```
$ cat ansible.cfg
[defaults]
host_key_checking = False
private_key_file = /Users/mkhan345/.ssh/my_aws
```
#### Running the playbook now
```
$ ansible-playbook playbook.yml --ask-vault-pass
```
```bash
PLAY RECAP ***************************************************************************
50.18.240.116              : ok=3    changed=2
localhost                  : ok=6    changed=1
```
Copying the script to EC2 server
```bash
scp -p -i ~/.ssh/my_aws list_instances.py ec2-user@ec2-50-18-240-116.us-west-1.compute.amazonaws.com:
```
### Running the python script in EC2 instance
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
[MIT](https://choosealicense.com/licenses/mit/)
