'''
    You must replace <FMI_1> with the table name
'''

import boto3
import json


def batch_put(courseCatalog):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('<FMI>')
    with table.batch_writer() as batch:
        for course in courseCatalog:
            courseID = course['courseID']
            courseName = course['courseName']
            courseStartTime = course['courseStartTime']
            courseEndTime = course['courseEndTime']
            formatted_data  = {
                'courseID': courseID,
                'courseName': courseName,
                'courseStartTime': courseStartTime,
                'courseEndTime': courseEndTime,
            }
            if 'courseCategory' in course:
                formatted_data['category'] = course['courseCategory']
                print("Adding course category:", courseID, courseName)
            else:
                print("Adding course:", courseID, courseName)
                pass
           
            batch.put_item(Item=formatted_data)

   
if __name__ == '__main__':
    with open("allCourses.json") as json_file:
        courseCatalog = json.load(json_file)['courseCatalog_arr']
    batch_put(courseCatalog)