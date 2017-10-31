#!/usr/bin/env python

import boto3
import os
#import the create instance function and pass the instance_id to terminate_isnatnce function
import create_ec2

def terminate_instance(instance_id):
     # connect to the ec2 resource
     ec2 = boto3.resource('ec2')
     print(instance_id)
     print("stopping instances...")
     # stop the running instance based on the ID
     ec2.instances.filter(InstanceIds=instance_id).terminate()

res = create_ec2.create_instances()
print(res, "this is id")
terminate_instance(res)

