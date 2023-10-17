# import json
from dynamoAddMultiple import batch_put

# with open("allCourses_test.json") as json_file:
#     courseCatalog = json.load(json_file)['courseCatalog_arr']

courseCatalog = {'course_name': 'CSE1000', 'num_credits': '3', 'course_title': 'Computers in Modern Society', 'course_start': '10:10AM', 'course_end': '11:00AM', 'subject': 'CSE'}

def test_batch():
    assert(batch_put(courseCatalog) == "Adding course: CSE1000")