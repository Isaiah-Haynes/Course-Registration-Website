import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('courseCatalog') #please add a temporary course in courseCatalog for testing.
    
    #deletes course event['courseName'] from courseCatalog
    response = table.delete_item(
        Key={
            "course_name": event['courseName']
        }
    )
    msg = str(event['courseName']) + " has been deleted!!"
    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }