'''
    You must replace <FMI_1> with the table name
'''

import boto3, json


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
    #add correct path below
    with open("allCourses.json") as json_file:
        #all items in courseCatalog are strings that may include numbers, letters, and colons (:)
        courseCatalog = json.load(json_file)['courseCatalog_arr']
    batch_put(courseCatalog)

"""
Copyright @2021 [Amazon Web Services] [AWS]
    
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
