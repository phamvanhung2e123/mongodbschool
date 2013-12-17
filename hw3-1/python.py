import pymongo
import sys
import pprint
from operator import itemgetter, attrgetter

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.school
students = db.students


def delete_lowest_score():
    print "students nice?! look at these scores now!"

    track = -1

    try:
        cursor = students.find()

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in cursor:
            print "before"
            pprint.pprint(doc)
            new_scores = sorted(doc["scores"],cmp = score_compare)
            new_scores.pop()
            doc["scores"]= new_scores
            students.save(doc)
            print "after"
            pprint.pprint(students.find_one(doc))


def score_compare(x, y):
    return (int)(y["score"] -x["score"]);

delete_lowest_score()
