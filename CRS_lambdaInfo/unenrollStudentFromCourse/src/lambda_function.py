import json
import boto3

def lambda_handler(event, context):
    course_name = event['course_name']
    studentID = event['id']
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    # get course
    courseCatalog = dynamodb.Table('courseCatalog')
    response = courseCatalog.get_item(Key={
        "course_name": course_name
    })
    # error - course not found - bad id (should never be tripped!!)
    if("Item" not in response):
        return {
            'statusCode': 200,
            'body': json.dumps("Course not found - something went wrong on our end, sorry!")
        }
    course = response["Item"]
    
    # get student
    studentList = dynamodb.Table('students')
    response = studentList.get_item(Key={
        "id": studentID
    })
    # error - student not found - bad id
    if("Item" not in response):
        return {
            'statusCode': 200,
            'body': json.dumps("Student not found - check your ID input!")
        }
    
    student = response["Item"]
    
    # error - student not enrolled
    if(course_name not in student["enrolled_courses"]):
        return {
            'statusCode': 200,
            'body': json.dumps("Unenroll FAILED - You are not enrolled in this course!")
        }
        
    # update enrollment numbers and number of credits
    updateEnrolledCredits = str(int(student["enrolled_credits"])-int(course["num_credits"])) 
    updated_enrollment = str(course["current_enrollment"]-1)
    
    db = boto3.client("dynamodb")
    db.update_item(TableName="students",
    Key={'id':{'S': studentID}},
    UpdateExpression="DELETE enrolled_courses :course SET enrolled_credits = :credits",
    ExpressionAttributeValues={
        ":course":{"SS":[course_name]},
        ":credits":{"N":updateEnrolledCredits}
    })
    
    db.update_item(TableName="courseCatalog",
    Key={'course_name':{'S': course_name}},
    UpdateExpression="SET current_enrollment = :enrollment",
    ExpressionAttributeValues={
        ":enrollment":{"N":updated_enrollment}
    })
    return {
        'statusCode': 200,
        'body': json.dumps("Unenroll SUCCESSFUL - You have been unenrolled!")
    }
