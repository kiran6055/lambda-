import json
import boto3
client = boto3.client('dynamodb')
def lambda_handler(event, context):
    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'CustomerID',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'Product',
                'AttributeType': 'S',
            },

        ],
        TableName='RetailSales02032022',
        KeySchema=[
            {
                'AttributeName': 'CustomerID',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'Product',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
       )
  
    print(response)