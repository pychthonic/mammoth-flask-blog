from flask_wtf import FlaskForm

from wtforms import IntegerField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import NumberRange
from wtforms.validators import Regexp


state_choices = [
		("PA", "Pennsylvania"), ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"),
		("AR", "Arkansas"), ("CA", "California"), ("CO", "Colorado"),
		("CT", "Connecticut"), ("DE", "Delaware"), ("FL", "Florida"),
		("GA", "Georgia"), ("HI", "Hawaii"), ("ID", "Idaho"),
		("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
		("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"),
		("ME", "Maine"), ("MD", "Maryland"), ("MA", "Massachusetts"),
		("MI", "Michigan"), ("MN", "Minnesota"), ("MS", "Mississippi"),
		("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"),
		("NV", "Nevada"), ("NH", "New Hampshire"), ("NJ", "New Jersey"),
		("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"),
		("ND", "North Dakota"), ("OH", "Ohio"), ("OK", "Oklahoma"),
		("OR", "Oregon"), ("RI", "Rhode Island"),
		("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"),
		("TX", "Texas"), ("UT", "Utah"), ("VT", "Vermont"),
		("VA", "Virginia"), ("WA", "Washington"), ("WV", "West Virginia"),
		("WI", "Wisconsin"), ("WY", "Wyoming")
		]


class CheesesteakForm(FlaskForm):
	street_address = StringField(
			'Street Address (ex: 500 South St)',
			validators=[
			DataRequired(),
			Length(max=50, message="That's a novel, not an address"),
			Regexp(regex="^[a-zA-Z0-9\s]*$", message="Letters, numbers, and spaces only")])
	city = StringField(
			'City or Town',
			default="Philadelphia",
			validators=[
			DataRequired(),
			Length(max=50),
			Regexp(regex="^[a-zA-Z\s]*$", message="Letters and spaces only")])
	state = SelectField('State',
			choices=state_choices,
			default=("PA", "Pennsylvania"),
			validators=[
			DataRequired(),
			Length(max=2),
			Regexp(regex="^[A-Z\s]{2}$")])
	how_many_blocks = IntegerField(
			'How many blocks would you travel for cheesesteak?',
			default=5,
			validators=[
			DataRequired(),
			NumberRange(
			min=0, max=500, message="Enter number between 1 and 500")])
	max_results = IntegerField(
			'Max number of results?',
			default=5,
			validators=[
			DataRequired(),
			NumberRange(
			min=1, max=40, message="Enter number between 1 and 30")])
	submit = SubmitField('Find me a Cheesesteak')

