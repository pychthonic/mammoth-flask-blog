from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email


class VolunteerForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(max=20)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
	phone_number = StringField('Phone Number', validators=[Length(max=20)])
	volunteer_email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
	street_addy = StringField('Street Address', validators=[Length(max=50)])
	apt_suite_bldg = StringField('Apt / Suite / Bldg', validators=[Length(max=20)])
	volunteer_city = StringField('City', validators=[Length(max=50)])
	volunteer_state = StringField('State / Province / Region', validators=[Length(max=50)])
	volunteer_zip = StringField('Postal / Zip Code', validators=[Length(max=20)])
	volunteer_country = StringField('Country', validators=[Length(max=20)])
	reporting = BooleanField('Reporting')
	project_leadership = BooleanField('Project Leadership')
	writing_and_editing = BooleanField('Writing & Editing')
	outreach = BooleanField('Neighborhood Outreach')
	social_media = BooleanField('Social Media')
	office_help = BooleanField('Office Help')
	legal = BooleanField('Legal')
	fundraising = BooleanField('Fundraising')
	other_volunteering_deets = TextField("Other ways I can help that aren't listed above:", validators=[Length(max=200)])
	submit = SubmitField('Submit')


class MemberForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(max=20)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
	phone_number = StringField('Phone Number', validators=[Length(max=20)])
	member_email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
	street_addy = StringField('Street Address', validators=[Length(max=50)])
	apt_suite_bldg = StringField('Apt / Suite / Bldg', validators=[Length(max=20)])
	member_city = StringField('City', validators=[Length(max=50)])
	member_state = StringField('State / Province / Region', validators=[Length(max=50)])
	member_zip = StringField('Postal / Zip Code', validators=[Length(max=20)])
	member_country = StringField('Country', validators=[Length(max=20)])
	submit = SubmitField('Submit')


class EmailListForm(FlaskForm):
	email_address_to_add = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
	submit = SubmitField('Submit')