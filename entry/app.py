from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from Grade import Grade

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

# Testing adding a grade
session = DB_SESSION()
grade = Grade('COMP 3495', 'Manraj', 'Bhullar', 95.2)
session.add(grade)
session.commit()
session.close()
