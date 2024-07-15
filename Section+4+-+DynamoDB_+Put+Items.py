import json
import boto3
client = boto3.client('dynamodb')
def lambda_handler(event, context):
   response = client.put_item(
        TableName='RetailSales02032022',
        Item = {
            'CustomerID': {
                'S': '2321',
            },
            'Product': {
                'S': 'Mango',
            },
            'Quantity': {
                'S': '10',
            },
            'Address': {
                'S': '1616 Prestige Tranquility',
            },
        },
   )
   
   print(response)


