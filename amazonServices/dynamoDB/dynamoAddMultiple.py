'''
    You must replace <courseCatalgo> with the table name (line 11)
'''

import json
import boto3
import sys

def check_args():
    if len(sys.argv) == 2:
        return 1
    else:
        return 0

def batch_put(courseCatalog):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('courseCatalog')
    with table.batch_writer() as batch:
        for course in courseCatalog:
            course_name = course['course_name']
            num_credits = course['num_credits']
            course_title = course['course_title']
            course_start = course['course_start']
            course_end = course['course_end']
            course_days = course['course_days']
            subject= course['subject']
            formatted_data  = {
                'course_name': course_name,
                'num_credits': num_credits,
                'course_title': course_title,
                'course_start': course_start,
                'course_end': course_end,
                'course_days': course_days,
                'subject': subject
            }

            print("Adding course:", course_name, course_title)

            batch.put_item(Item=formatted_data)
    #return "Adding course: "+course_name

   
if __name__ == '__main__':
    if check_args() and ".json" in sys.argv[1]:
        inputFile = sys.argv[1]
    else:
        print("Usage: python3 dynamoAddMultiple.py <input json file>")
        exit()
    with open(inputFile) as json_file:
        courseCatalog = json.load(json_file)['courseCatalog_arr']
    batch_put(courseCatalog)