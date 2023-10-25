import boto3, json
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Key, Attr, Not
import sys

def check_args():
    if len(sys.argv) == 4:
        return 1
    else:
        print("usage: python3 filterTable.py <tableName> <tableColumn> <filter>")
        return 0


def scanTable(tableName, tableColumn, filter):
    
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table(tableName)

    response = table.scan(
        FilterExpression = Attr(tableColumn).contains(filter)
    )
        
    data = response['Items']
    courses = []
    for course in data:
        courses.append(course['course_name'])
        print(course['course_name'])
    # print(courses)
    return courses
 
if __name__ == '__main__':
    if check_args() == 0:
        exit()
    scanTable(sys.argv[1], sys.argv[2], sys.argv[3])