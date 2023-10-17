This is the temporary README for AWS info.

"dynamoAddMultiple.py" will be used to add all of the courses from an input json file to a DynamoDB table. The name of said DynamoDB table is currently "CourseCatalog" and will need to be changed if the dynamoDB table name on AWS is changed. dynamoAddMultiple.py takes a json input file and places them in a dynamoDB table. An example of its proper use with cseCourses.json is included below.
```sh
python3 dynamoAddMultiple.py cseCourses.json
```
This is so that different lists of courses can be worked on at the same time by multiple members. It will also enable the use of multiple smaller files instead of one large file.