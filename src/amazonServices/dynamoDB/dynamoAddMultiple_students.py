import json
import boto3
import sys

#checks that there is an argument given when file is run
def check_args():
    if len(sys.argv) == 2:
        return 1
    else:
        return 0

def batch_put(students):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('students')
    with table.batch_writer() as batch:
        for student in students:
            #give variable names to the items in json file
            id = student['id']
            name = student['name']
            major = student['major']
            minor = student['minor']
            standing = student['standing']
            gpa = student['gpa']
            total_credits = student['total_credits']
            enrolled_credits = student['enrolled_credits']
            enrolled_courses = student['enrolled_courses']
            past_courses = student['past_courses']
            
            #formats the data read back to json to put in table
            formatted_data  = {
                'id': id,
                'name': name,
                'major': major,
                'minor': minor,
                'standing': standing,
                'gpa': gpa,
                'total_credits': total_credits,
                'enrolled_credits': enrolled_credits,
                'enrolled_courses': enrolled_courses,
                'past_courses': past_courses
            }

            print("Adding student: "+id+" - "+name)

            #puts student in dynamoDB table
            batch.put_item(Item=formatted_data)

            print("Added student: "+id+" - "+name)

   
if __name__ == '__main__':

    #checks that the correct argument is given when file is run
    if check_args() and ".json" in sys.argv[1]:
        inputFile = sys.argv[1]
    else:
        print("Usage: python3 dynamoAddMultiple_students.py <input json file>")
        exit()
    
    #opens json file from given argument
    with open(inputFile) as json_file:
        students = json.load(json_file)['students_arr']
    batch_put(students)