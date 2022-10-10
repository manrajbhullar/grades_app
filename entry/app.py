from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from Grade import Grade
from flask import Flask, render_template, request
from GradeForm import GradeForm
import requests

# DB Credentials
DB_HOST = 'entry_db'
DB_PORT = '3306'
DB_USER = 'grades_app'
DB_PASSWORD = 'grades_app'
DB_NAME = 'grades_app'

# DB Connection
DB_ENGINE = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

ANALYTICS_IP = 'analytics'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def enter_grade():

    form = GradeForm(request.form)
    if request.method == 'POST':
        if form.validate():
            
            grade = Grade(form.course.data, form.first_name.data, form.last_name.data, form.grade.data)
            session = DB_SESSION()
            session.add(grade)
            session.commit()
            session.close()

            requests.get(f'http://{ANALYTICS_IP}:8100/update_stats')
            return render_template('index.html')
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')
