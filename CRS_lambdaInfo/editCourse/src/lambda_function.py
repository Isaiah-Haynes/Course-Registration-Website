import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # edit a table item and update it in the db
    
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    update_expression = 'SET '
    expression_attribute_values = {}

    for attribute_name, attribute_value in event.items():
        if attribute_name != 'course_name':
            if (attribute_value == ''):
                continue
            placeholder = f':{attribute_name}'
            update_expression += f'{attribute_name} = {placeholder}, '
            
            if isinstance(attribute_value, str):
                expression_attribute_values[placeholder] = {'S': attribute_value}
            elif isinstance(attribute_value, int):
                expression_attribute_values[placeholder] = {'N': str(attribute_value)}
    
    update_expression = update_expression.rstrip(', ')
    
    try:
        response = DDB.update_item(
            TableName= 'courseCatalog', 
            Key={'course_name': {'S': event['course_name']}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
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

