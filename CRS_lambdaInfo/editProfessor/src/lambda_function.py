import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # edit a table item and update it in the db
    # NOTE: cannot edit attribute 'name' as it is a reserved keyword and will not work
    # when testing, and in use, do not edit the attribute name
    
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    update_expression = 'SET '
    expression_attribute_values = {}

    for attribute_name, attribute_value in event.items():
        if attribute_name != 'id':
            if (attribute_value == '') or (attribute_value == []) or (attribute_value == [""]):
                continue
            placeholder = f':{attribute_name}'
            update_expression += f'{attribute_name} = {placeholder}, '
            
            if isinstance(attribute_value, str):
                expression_attribute_values[placeholder] = {'S': attribute_value}
            elif isinstance(attribute_value, list):
                expression_attribute_values[placeholder] = {'SS': attribute_value}
    
    update_expression = update_expression.rstrip(', ')
    
    try:
        response = DDB.update_item(
            TableName= 'professors', 
            Key={'id': {'S': event['id']}},
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
