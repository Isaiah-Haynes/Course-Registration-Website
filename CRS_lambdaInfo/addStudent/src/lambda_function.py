import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            TableName= "students",
            Item={
                'id': {
                    'S': event['id']
                },
                'name': {
                    'S': event['name']
                },
                'major': {
                    'S': event['major']
                },
                'minor': {
                    'S': event['minor']
                },
                'standing': {
                    'S': event['standing']
                },
                'gpa': {
                    'S': event['gpa']
                },
                'total_credits': {
                    'N': event['total_credits']
                },
                'enrolled_credits': {
                    'N': event['enrolled_credits']
                },
                'enrolled_courses': {
                    'SS': event['enrolled_courses']
                },
                'past_courses': {
                    'SS': event['past_courses']
                }
            },
            ConditionExpression='attribute_not_exists(id)'
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response)
            }
        
    except ClientError as e:
    # Ignore the ConditionalCheckFailedException, bubble up
    # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise
