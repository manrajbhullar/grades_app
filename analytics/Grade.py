from sqlalchemy import Column, Integer, Float, String
from base import Base

class Grade(Base):
    """ Grade """

    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(String(25), nullable=False)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    grade = Column(Float, nullable=False)

    def __init__(self, course, first_name, last_name, grade):
        """ Initializes a Grade object """
        self.course = course
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def to_dict(self):
        """ Dictionary representation of a workout summary event """
        dict = {}
        dict['id'] = self.id
        dict['course'] = self.course
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['grade'] = self.grade

        return dict
