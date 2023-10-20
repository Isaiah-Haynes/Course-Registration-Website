README

dynamoAddMultiple.py


"dynamoAddMultiple.py" will be used to add all of the courses from an input json file to a DynamoDB table. dynamoAddMultiple.py takes a json input file and places its contents into a dynamoDB table. An example of its proper use with cseCourses.json is included below.
```sh
python3 dynamoAddMultiple.py cseCourses.json
```
When adding non-CSE courses, they can be added to a different json file which will then be used as input to "dynamoAddMultiple.py".

The format for each course in "cseCourses.json" should be replicated as follows:
{
    "course_name": "course_name e.g. CSE1000", (str)
    "num_credits": "number of credits", (int)
    "course_title": "title of course", (str)
    "course_start": "course start time in format 12:00PM", (str)
    "course_end": "course end time in format 12:00PM", (str)
    "course_days": "days of course e.g. 'M W F'", (str)
    "subject": "course subject e.g. CSE", (str)
    "professor": "course professor e.g. John Smith", (str)
    "max_enrollment": "maximum number of students in course", (int)
    "current_enrollment": "numbe of students currently enrolled in course" (int)
}


createTable.py


"createTable.py" will be used to create a new table. This table can either be for the courses a specific student is taking, or the courses that a specific professor is teaching. It takes as input the name of the table to be created. Any courses added to this table should be in the same format as defined above for "dynamoAddMultiple.py". The title of the table must contain "-courses" in it as shown in the example below. 
```sh
python3 createTable.py isaiah-courses
```
The above command will create a new dynamoDB table with the name "isaiah-courses" as long as it does not already exist.