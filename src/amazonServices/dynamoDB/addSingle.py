import boto3
from botocore.exceptions import ClientError
import sys

def check_args():
    if len(sys.argv) == 12:
        return 1
    else:
        print("usage:")
        print("python3 addSingle.py course_name num_credits course_title course_start course_end course_days subject professor max_enrollment current_enrollment Table_name")
        return 0

def addSingleConditional(course_parameters):
    
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            TableName= course_parameters[10],
            Item={
                'course_name': {
                    'S': course_parameters[0]
                },
                'num_credits': {
                    'N': course_parameters[1]
                },
                'course_title':{
                    'S': course_parameters[2] #number passed in as a string (ie in quotes)
                },
                'course_start':{
                    'S': course_parameters[3]
                },
                'course_end':{
                    'S': course_parameters[4]
                },
                'course_days':{
                    'S': course_parameters[5]
                },
                'subject':{
                    'S': course_parameters[6]
                },
                'professor':{
                    'S': course_parameters[7]
                },
                'max_enrollment':{
                    'N': course_parameters[8]
                },
                'current_enrollment':{
                    'N': course_parameters[9]
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
    if check_args() == 0: 
        exit()
    courseParameters = []
    for i in range(1, 12):
        courseParameters.append(sys.argv[i])
    addSingleConditional(courseParameters)
    print('Done')