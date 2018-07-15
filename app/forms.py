from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired

class HomeForm(FlaskForm):
    start_location = StringField('Starting Location',
        validators=[DataRequired()])
    end_location = StringField('Ending Location',
        validators=[DataRequired()])
    start_time = DateTimeField('Start Time',
        format='%H:%M:%S',
        validators=[DataRequired()])
    end_time = DateTimeField('End Time',
        format='%H:%M:%S',
        validators=[DataRequired()])
    budget = IntegerField('Story Budget')