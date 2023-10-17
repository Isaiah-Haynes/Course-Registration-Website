import json
from dynamoAddMultiple import batch_put

def test_batch():
    assert(batch_put(courseCatalog) == "Adding course: CSE1000")

if __name__ == '__main__':
    with open("allCourses_test.json") as json_file:
        courseCatalog = json.load(json_file)['courseCatalog_arr']
    batch_put(courseCatalog)