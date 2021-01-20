from datetime import datetime, date
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, widgets, DateField
from wtforms.validators import DataRequired, AnyOf, URL
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class ActorForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    age = StringField(
        'age', validators=[DataRequired()]
    )
    gender = SelectField(
        'gender', validators=[DataRequired()],
        choices=[
            ('female', 'female'),
            ('male', 'male')]
    )

class MovieForm(Form):
    title = StringField(
        'title', validators=[DataRequired()]
    )
    release = DateField(
        'release',
        validators=[DataRequired()],
        default= date.today()
    )
