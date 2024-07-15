# here we are using to send files stroed in s3 bucket test6055 file (key) name DynamoDB_Samplefile inserting it in dynamo db table
#first the objects in s3 will be converted into streamingbody ojbect we have to convert it into bytes and json and finally dict format to insert in dynamdb table salesjuly


import json
import boto3

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    response = client.get_object(
        Bucket='test6055',
        Key='DynamoDB_Samplefile.json',
    )
    
    json_data = response['Body'].read()
    print(type(json_data))
    
    # converting streaming body into byte first
    # we use "variablename".decode('UTF-8') from byte to streaming body variablename.encode('utf-8')
    data_string = json_data.decode('UTF-8')
    print(type(data_string))
    
    # converting a datatype from json to dictionary using json.loads()
    data_dict = json.loads(data_string)
    print(type(data_dict))
    
    # inserting data into DynamoDB table
    table = dynamodb.Table('salesjuly')
    table.put_item(
        Item=data_dict
    )

#this we have to use if we have more files we need to use this
import json
import boto3

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # List all objects in the S3 bucket
    response = client.list_objects_v2(
        Bucket='test6055'
    )
    
    for obj in response.get('Contents', []):
        # Get each object's content
        obj_response = client.get_object(
            Bucket='test6055',
            Key=obj['Key']
        )
        
        # Read and decode the JSON content
        json_data = obj_response['Body'].read().decode('utf-8')
        
        # Convert JSON to dictionary
        data_dict = json.loads(json_data)
        
        # Insert data into DynamoDB table
        table = dynamodb.Table('salesjuly')
        table.put_item(
            Item=data_dict
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted into DynamoDB')
    }





