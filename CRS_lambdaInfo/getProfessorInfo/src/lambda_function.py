import json
import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Key, Attr, Not

def lambda_handler(event, context):
    id = event['id']
    
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('professors')
    response = table.scan(
        FilterExpression = Attr('id').contains(id)
    )
    professor = response['Items'][0]
    
    professor_info = []
    # 0: id                     primary key
    # 1: name                   use on greeting/displaying professor info
    # 2: department             use when displaying professor info
    # 3: current_courses        use for schedule view
    professor_info.append(professor['id'])
    professor_info.append(professor['name'])
    professor_info.append(professor['department'])
    professor_info.append(list(professor['current_courses'])) # any sets need to be cast into lists
    
    # return professor info
    return {
        "professor": professor_info
    }