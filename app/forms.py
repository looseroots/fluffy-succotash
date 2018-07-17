from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, TimeField
from datetime import datetime

class HomeForm(FlaskForm):
    time_format = '%Y-%m-%d %H:%M'

    now = datetime.now().strftime(time_format)

    start_location = StringField('Starting Location',
        validators=[DataRequired()])
    end_location = StringField('Ending Location',
        validators=[DataRequired()])
    start_date = DateField('Story Date', format='%m-%d')
    start_time = TimeField('Start Time', format=time_format)
    end_time = TimeField('End Time', format=time_format)
    budget = IntegerField('Story Budget')