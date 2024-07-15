import json
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
   listbucket=client.list_buckets()
   total=len(listbucket['Buckets'])
   print(total)
   if total > 0:
      for buckets in listbucket['Buckets']:
         name = buckets['Name']
         date = buckets['CreationDate']
         print(f"bucketname: {name} - creationdate: {date}")
   else:
      print("no Buckets found")