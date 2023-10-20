import json
import boto3
import sys

#checks that there is an argument given when file is run
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
            #give variable names to the items in json file
            course_name = course['course_name']
            num_credits = course['num_credits']
            course_title = course['course_title']
            course_start = course['course_start']
            course_end = course['course_end']
            course_days = course['course_days']
            subject = course['subject']
            professor = course['professor']
            max_enrollment = course['max_enrollment']
            current_enrollment = course['current_enrollment']
            
            #formats the data read back to json to put in table
            formatted_data  = {
                'course_name': course_name,
                'num_credits': num_credits,
                'course_title': course_title,
                'course_start': course_start,
                'course_end': course_end,
                'course_days': course_days,
                'subject': subject,
                'professor': professor,
                'max_enrollment': max_enrollment,
                'current_enrollment': current_enrollment
            }

            print("Adding course: "+course_name+" - "+course_title)

            #puts course in dynamoDB table
            batch.put_item(Item=formatted_data)

   
if __name__ == '__main__':

    #checks that the correct argument is given when file is run
    if check_args() and ".json" in sys.argv[1]:
        inputFile = sys.argv[1]
    else:
        print("Usage: python3 dynamoAddMultiple.py <input json file>")
        exit()
    
    #opens json file from given argument
    with open(inputFile) as json_file:
        courseCatalog = json.load(json_file)['courseCatalog_arr']
    batch_put(courseCatalog)