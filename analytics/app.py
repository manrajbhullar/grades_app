from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from Grade import Grade
from flask import Flask
from mongoengine import connect
from Stats import Results, CourseStats
from datetime import datetime

# DB Config for MySQL
MYSQL_HOST = 'entry_db'
MYSQL_PORT = '3306'
MYSQL_USER = 'grades_app'
MYSQL_PASSWORD = 'grades_app'
MYSQL_DBNAME = 'grades_app'
DB_ENGINE = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DBNAME}")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

# DB Config for MongoDB
MONGO_HOST = 'results_db'
MONGO_PORT = 27017
MONGO_DBNAME = 'grades_app'
CONN_STR = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}'
connect(host=CONN_STR)

app = Flask(__name__)

@app.route('/update_stats', methods=['GET'])
def update_stats():
    # Get Previous Amount of Grades
    if len(Results.objects()) > 0:
        previous_results = list(Results.objects())[-1]
        previous_num_grades = previous_results.num_grades
    else:
        previous_num_grades = 0

    # Get Grades from MySQL
    session = DB_SESSION()
    grades_query = session.query(Grade).all()
    session.close()

    # Set Current Amount of Grades
    num_grades = len(grades_query)

    # Update stats if a new grade has been added
    if num_grades > previous_num_grades and num_grades > 0:
        grades = []
        for grade in grades_query:
            grades.append(grade.to_dict())

        # Calculate Stats for All Courses
        courses = []
        for grade in grades:
            courses.append(grade['course'])
        courses = set(courses)

        stats = []
        for course in courses:
            course_grades = []
            for grade in grades:
                if grade['course'] == course:
                    course_grades.append(grade['grade'])
            course_avg_grade = round(sum(course_grades)/len(course_grades), 1)
            course_min_grade = min(course_grades)
            course_max_grade = max(course_grades)
            course_stats = {'course_name': course, 'avg': course_avg_grade, 'min': course_min_grade, 'max': course_max_grade, 'timestamp': datetime.now()}
            stats.append(course_stats)

        # Store Latest Stats in MongoDB
        course_objects = []
        for stats_for_course in stats:
            course = CourseStats()
            course.name = stats_for_course['course_name']
            course.avg = stats_for_course['avg']
            course.min = stats_for_course['min']
            course.max = stats_for_course['max']
            course.timestamp = stats_for_course['timestamp']
            course.save()
            course_objects.append(course)

        results = Results()
        results.courses = course_objects
        results.num_grades = num_grades
        results.timestamp = datetime.now()
        results.save()
    
    return '200'


if __name__ == "__main__":
    app.run(port=8100, host='0.0.0.0')