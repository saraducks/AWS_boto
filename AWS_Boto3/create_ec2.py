#!/usr/bin/env python

import boto3

def create_instances():
    ec2 = boto3.resource('ec2')

    # create the instance of the type ami-e689729e
    temp = ec2.create_instances(ImageId='ami-e689729e', MinCount=1, MaxCount=1,InstanceType='t2.micro')
    return temp[0].id

create_instances()




