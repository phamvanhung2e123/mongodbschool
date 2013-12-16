import pymongo
import sys
import pprint
connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.school
students = db.students

def delete_lowest_score():

	print "students nice?! look at these scores now!"

	track = -1

	try:
		cursor = grades.find()

	except:
		print "Unexpected error:", sys.exc_info()[0]

	for doc in cursor:
		if doc['student_id'] != track:
            pprint.pprint(doc)

delete_lowest_score()
