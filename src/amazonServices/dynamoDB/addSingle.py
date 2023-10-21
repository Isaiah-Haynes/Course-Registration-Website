import boto3
from botocore.exceptions import ClientError

def check_args():
    if len(sys.argv) == 2:
        return 1
    else:
        return 0

def conditional_put():
    
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            TableName='<FMI_1>',
            Item={
                'course_name': {
                    'S': '<FMI_2>'
                },
                'num_credits': {
                    'N': '<FMI_3>'
                },
                'course_title':{
                    'N': '<FMI_4>' #number passed in as a string (ie in quotes)
                },
                'course_start':{
                    'S': '<FMI_5>'
                },
                'course_end':{
                    'S': '<FMI_5>'
                },
                'course_days':{
                    'S': '<FMI_5>'
                },
                'subject':{
                    'S': '<FMI_5>'
                },
                'professor':{
                    'S': '<FMI_5>'
                },
                'max_enrollment':{
                    'N': '<FMI_5>'
                },
                'current_enrollment':{
                    'N': '<FMI_5>'
                },
            },
            ConditionExpression='attribute_not_exists(course_name)'
        )
    except ClientError as e:
        # Ignore the ConditionalCheckFailedException, bubble up
        # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise

if __name__ == '__main__':
    conditional_put()
    print('Done')