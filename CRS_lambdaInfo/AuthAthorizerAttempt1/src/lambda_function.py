import json

def lambda_handler(event, context):
    # TODO implement
    response_data = {
        "message": "Success! You accessed the REST API"
    }
    
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(response_data)
    }
    return response
