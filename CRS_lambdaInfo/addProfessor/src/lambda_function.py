import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            TableName= "professors",
            Item={
                'id': {
                    'S': event['id']
                },
                'name': {
                    'S': event['name']
                },
                'department': {
                    'S': event['department']
                },
                'current_courses': {
                    'SS': event['current_courses']
                }
            },
            ConditionExpression='attribute_not_exists(id)'
        )
        return response
        
    except ClientError as e:
    # Ignore the ConditionalCheckFailedException, bubble up
    # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise
