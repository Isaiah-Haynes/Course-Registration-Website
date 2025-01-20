import json
import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Key, Attr, Not

def lambda_handler(event, context):
    id = event['id']
    
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('students')
    response = table.scan(
        FilterExpression = Attr('id').contains(id)
    )
    # error - course not found - bad id (should never be tripped!!)
    if("Items" not in response):
        return {
            'statusCode': 200,
            'body': json.dumps("Student not found - something went wrong on our end, sorry!")
        }
    student = response['Items'][0]
    
    student_info = []
    # 0: id                     primary key
    # 1: name                   use on greeting/displaying student info
    # 2: major                  use when displaying student info
    # 3: minor                  use when displaying student info
    # 4: standing               use when displaying student info
    # 5: gpa                    use when displaying student info
    # 6: total_credits          use when displaying student info
    # 7: enrolled_credits       use for enrollment validity + display
    # 8: enrolled_courses       use for schedule view + enrollment validity
    # 9: past_courses           use if implementing prereqs
    student_info.append(student['id'])
    student_info.append(student['name'])
    student_info.append(student['major'])
    student_info.append(student['minor'])
    student_info.append(student['standing'])
    student_info.append(student['gpa'])
    student_info.append(student['total_credits'])
    student_info.append(student['enrolled_credits'])
    student_info.append(list(student['enrolled_courses'])) # any sets need to be cast into lists
    student_info.append(list(student['past_courses']))
    
    # return student info
    return {
        "student": student_info
    }