from flask import flash
from flask_wtf import FlaskForm

from wtforms import IntegerField
from wtforms import StringField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import NumberRange
from wtforms.validators import Regexp


class CheesesteakForm(FlaskForm):
	street_number = IntegerField(
			'Street Number', validators=[
			DataRequired(),
			NumberRange(min=0, max=50000, message="Invalid street number"),
			])
	street_name = StringField(
			'Street Name',
			validators=[DataRequired(), Length(max=60)],
			Regexp(regex="^[a-zA-Z\s]*$", message="Letters and spaces only"))
	submit_new = SubmitField('Create Post')
	submit_update = SubmitField('Submit')