import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.students
grades = db.grades


def delete_lowest_score():
    print "grading nice?! look at these scores now!"



    query = {'type': 'homework'}
    sort = [('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)]
    track = -1

    try:
        cursor = grades.find(query).sort(sort)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in cursor:
        if doc['student_id'] != track:
            grades.remove(doc)
            print "grading nice?! look at these scores now!"
            track = doc['student_id']

delete_lowest_score()
