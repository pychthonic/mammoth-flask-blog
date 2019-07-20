from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import Length


class LoginForm(FlaskForm):
	email = StringField(
			'Email',
			validators=[DataRequired(), Email(), Length(max=30)])
	password = PasswordField(
			'Password',
			validators=[DataRequired(), Length(max=20)])
	submit = SubmitField('Login')