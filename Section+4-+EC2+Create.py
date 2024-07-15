import json
import boto3
client = boto3.client('ec2')

def lambda_handler(event, context):
    
    response = client.run_instances(
    ImageId='ami-0a4e637babb7b0a86',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1)
    instances = response['Instances']
    #print(type(instances))
    for values in instances:
        print(values['InstanceId'])
    #print(type(values))