import json
import boto3
import sys

#checks that there is an argument given when file is run
def check_args():
    if len(sys.argv) == 2:
        return 1
    else:
        return 0

def batch_put(professors):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('professors')
    with table.batch_writer() as batch:
        for professor in professors:
            #give variable names to the items in json file
            id = professor['id']
            name = professor['name']
            department = professor['department']
            current_courses = set(professor['current_courses'])
            
            #formats the data read back to json to put in table
            formatted_data  = {
                'id': id,
                'name': name,
                'department': department,
                'current_courses': current_courses
            }

            print("Adding professor: "+id+" - "+name)

            #puts professor in dynamoDB table
            batch.put_item(Item=formatted_data)

            print("Added professor: "+id+" - "+name)

   
if __name__ == '__main__':

    #checks that the correct argument is given when file is run
    if check_args() and ".json" in sys.argv[1]:
        inputFile = sys.argv[1]
    else:
        print("Usage: python3 dynamoAddMultiple_professors.py <input json file>")
        exit()
    
    #opens json file from given argument
    with open(inputFile) as json_file:
        professors = json.load(json_file)['professors_arr']
    batch_put(professors)