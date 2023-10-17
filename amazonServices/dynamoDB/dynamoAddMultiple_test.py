import json
from dynamoAddMultiple import batch_put

with open("allCourses_test.json") as json_file:
    courseCatalog = json.load(json_file)['courseCatalog_arr']

def test_batch():
    assert(batch_put(courseCatalog) == "Adding course: CSE1000")