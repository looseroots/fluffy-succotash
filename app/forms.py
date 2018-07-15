from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class HomeForm(FlaskForm):
    location = StringField('location', validators=[DataRequired()])