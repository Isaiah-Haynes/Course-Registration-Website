README for dynamoAddMultiple

"dynamoAddMultiple.py" will be used to add all of the courses from an input json file to a DynamoDB table. dynamoAddMultiple.py takes a json input file and places its contents into a dynamoDB table. An example of its proper use with cseCourses.json is included below.
```sh
python3 dynamoAddMultiple.py cseCourses.json
```
When adding non-CSE courses, they can be added to a different json file which will then be used as input to "dynamoAddMultiple.py".

The format for each course in "cseCourses.json" should be replicated as follows: { "course_name": "course_name e.g. CSE1000", "num_credits": "number of credits", "course_title": "title of course", "course_start": "course start time in format 12:00PM", "course_end": "course end time in format 12:00PM", "course_days": "days of course e.g. 'M W F'", "subject": "course subject e.g. CSE" }