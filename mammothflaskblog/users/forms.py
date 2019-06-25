from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email#, ValidationError
#from flask_login import current_user
#from mammothflaskblog.models import User


class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email(), Length(max=30)])
	password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])
	submit = SubmitField('Login')