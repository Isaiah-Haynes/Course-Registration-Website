import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            #TableName= testTable, #for testing, use this table
            
            #for final website, use the following table
            TableName= "courseCatalog",
            Item={
                'course_name': {
                    'S': event['course_name']
                },
                'num_credits': {
                    'N': event['num_credits']
                },
                'course_title':{
                    'S': event['course_title']
                },
                'course_start':{
                    'S': event['course_start']
                },
                'course_end':{
                    'S': event['course_end']
                },
                'course_days':{
                    'S': event['course_days']
                },
                'subject':{
                    'S': event['subject']
                },
                'professor':{
                    'S': event['professor']
                },
                'max_enrollment':{
                    'N': event['max_enrollment']
                },
                'current_enrollment':{
                    'N': event['current_enrollment']
                },
            },
            ConditionExpression='attribute_not_exists(course_name)'
        )
        return response
    except ClientError as e:
        # Ignore the ConditionalCheckFailedException, bubble up
        # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise
