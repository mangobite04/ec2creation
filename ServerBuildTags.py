#!/usr/bin/env python

import boto3ec2 = boto3.resource('ec2', region_name='eu-west-1')

instance = ec2.create_instances(    
ImageId='ami-d834aba1',    
MinCount=1,    
MaxCount=1,    
InstanceType='t2.micro',    
KeyName='my_keypair_name',    
SecurityGroupIds=['sg-5dd3ca27'],    
SubnetId='subnet-01b05349')[0]

print (instance.id)

instance = instance.id
ec2.create_tags(Resources=[instance], Tags=[{'Key':'Name', 'Value':'AppHostName'}, {'Key':'Owner', 'Value':'Devesh'}, {'Key':'ENV', 'Value':'DTA'}])
