import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('professors')
    
    #deletes professor given id
    response = table.delete_item(
        Key={
            "id": event['id']
        }
    )
    msg = "Professor " + str(event['id']) + " has been deleted!!"
    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }