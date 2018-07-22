from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Optional
from wtforms.fields.html5 import DateField, TimeField

class HomeForm(FlaskForm):
    start_location = StringField('Starting Location', validators=[DataRequired()])
    end_location = StringField('Ending Location', validators=[DataRequired()])
    start_date = DateField('Story Date', validators=[Optional()])
    start_time = TimeField('Start Time', validators=[Optional()])
    end_time = TimeField('End Time', validators=[Optional()])
