import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(ACL='private', Bucket='my-boto-s3-demo',CreateBucketConfiguration={'LocationConstraint':'us-west-2'})

print(response)

