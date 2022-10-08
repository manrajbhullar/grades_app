from mongoengine import connect
from Stats import Results, CourseStats
from datetime import datetime

# DB Config
DB_HOST = 'results_db'
DB_PORT = 27017
DB_NAME = 'grades_app'
CONN_STR = f'mongodb://{DB_HOST}:{DB_PORT}/{DB_NAME}'
connect(host=CONN_STR)

# Creating some test stats
course1 = CourseStats()
course1.name = 'COMP 3495'
course1.avg = 80.2
course1.min = 59.2
course1.max = 97.1

course2 = CourseStats()
course2.name = 'COMP 3496'
course2.avg = 80.1
course2.min = 59.4
course2.max = 97.5

course3 = CourseStats()
course3.name = 'COMP 3497'
course3.avg = 80.3
course3.min = 59.3
course3.max = 97.5

course1.save()
course2.save()
course3.save()

courses = [course1, course2, course3]
results = Results()
results.courses = courses
results.timestamp = datetime.now()
results.save()

# Getting Latest Results
latest_results = list(Results.objects())[-1]
print(latest_results.timestamp)
for course in latest_results.courses:
    print(course.name, course.avg, course.min, course.max)