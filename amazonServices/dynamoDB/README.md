This is the temporary README for AWS info.

"allCourses.json" includes an array of all the courses used in our system.

"dynamoAddMultiple.py" (name subject to change) will be used to add all of the courses from "allCourses.json" to a DynamoDB table. The name of said DynamoDB table is currently "CourseCatalogTest" and will need to be changed when we make the actual final table. At a later date, this file may include separate functions to add multiple items or add a single item based on a single command. These functions may also be separate files to allow for multiple people working on them at a time. It is important to note that allCourses.json is not finished at this time.