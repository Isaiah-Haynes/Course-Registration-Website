import json
import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Key, Attr, Not

def lambda_handler(event, context):
    tableFilter = event['tableFilter']
    
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('courseCatalog')
    response = table.scan(
        FilterExpression = Attr('course_name').contains(tableFilter)
    )
    data = response['Items']
    
    response = table.scan(
        FilterExpression = Attr('course_title').contains(tableFilter)
    )
    
    for item in response['Items']:
        if item not in data:
            data.append(item)
            
    courses = []
    for course in data:
        # Each element in courses is a list of the course attributes
        # 0: course_name
        # 1: num_credits
        # 2: course_title
        # 3: course_start
        # 4: course_end
        # 5: course_days
        # 6: subject
        # 7: professor
        # 8: max_enrollment
        # 9: current_enrollment
        courses.append([course['course_name']])
        courses[len(courses)-1].append(course['num_credits'])
        courses[len(courses)-1].append(course['course_title'])
        courses[len(courses)-1].append(course['course_start'])
        courses[len(courses)-1].append(course['course_end'])
        courses[len(courses)-1].append(course['course_days'])
        courses[len(courses)-1].append(course['subject'])
        courses[len(courses)-1].append(course['professor'])
        courses[len(courses)-1].append(course['max_enrollment'])
        courses[len(courses)-1].append(course['current_enrollment'])
    return {
        "courses": courses
    }