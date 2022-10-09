from wtforms import Form, StringField, FloatField, validators

class GradeForm(Form):
    course = StringField('course', [validators.Length(min=1, max=25)])
    first_name = StringField('course', [validators.Length(min=1, max=25)])
    last_name = StringField('course', [validators.Length(min=1, max=25)])
    grade = FloatField('grade')