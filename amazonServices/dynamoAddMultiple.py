'''
    You must replace <FMI_1> with the table name
'''

import json
import boto3


def batch_put(courseCatalog):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('<FMI>')
    with table.batch_writer() as batch:
        for course in courseCatalog:
            course_name = course['course_name']
            course_title = course['course_title']
            num_credits = course['num_credits']
            course_start = course['course_start']
            course_end = course['course_end']
            course_category = course['course_category']
            formatted_data  = {
                'course_name': course_name,
                'course_title': course_title,
                'num_credits': num_credits,
                'courseStartTime': course_start,
                'courseEndTime': course_end,
                'course_category': course_category
            }

            print("Adding course:", course_name, course_title)
           
            batch.put_item(Item=formatted_data)

   
if __name__ == '__main__':
    with open("allCourses.json") as json_file:
        courseCatalog = json.load(json_file)['courseCatalog_arr']
    batch_put(courseCatalog)