from mongoengine import Document, ListField, ReferenceField, StringField, IntField, FloatField, DateTimeField

class Results(Document):
    courses = ListField(ReferenceField('CourseStats'), required=True)
    num_grades = IntField(required=True)
    timestamp = DateTimeField(required=True)
    
    meta = {
        'collection': 'results'
    }

class CourseStats(Document):
    name = StringField(required=True)
    avg = FloatField(required=True)
    min = FloatField(required=True)
    max = FloatField(required=True)
    timestamp = DateTimeField(required=True)
    
    meta = {
        'collection': 'course_stats'
    }