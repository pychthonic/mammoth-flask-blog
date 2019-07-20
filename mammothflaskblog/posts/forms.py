from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FieldList
from wtforms import FileField
from wtforms import MultipleFileField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Optional
from wtforms.validators import StopValidation
from wtforms.validators import URL

from collections import Iterable


class MultiFileAllowed(object):
	"""This class is used to check the validity of additional files
	uploaded to a post, checking that they are certain types. See
	extra_photos attribute in the PostForm class below.
	"""
	def __init__(self, upload_set, message=None):
		self.upload_set = upload_set
		self.message = message
	def __call__(self, form, field):
		for data in field.data:
			if not isinstance(data, str):
				filename = data.filename.lower()
				if isinstance(self.upload_set, Iterable):
					if filename.split('.')[1] not in self.upload_set:
						flash(f"File does not have approved extension: {', '.join(
								self.upload_set)}", 'error')
						raise StopValidation(
								self.message or field.gettext(
								f"File does not have approved extension: {', '.join(
								self.upload_set)}"))


class PostForm(FlaskForm):
	title = StringField(
			'Title', validators=[DataRequired(), Length(max=100)])
	content = TextAreaField(
			'Content (Note: No links in Content section!)',
			validators=[DataRequired(), Length(max=25000)])
	main_photo = FileField(
			'Main Photo',
			validators=[FileAllowed(['jpg', 'jpeg', 'png'],
			'File must be .jpg, .jpeg or .png. Consult webmaster if you have a question about converting.')])
	main_photo_caption = StringField('Main Photo Caption', 
									 validators=[Length(max=150)])
	extra_photos = MultipleFileField(
			'Additional Photos',
			default=None,
			validators=[MultiFileAllowed(['jpg', 'jpeg', 'png'])])
	extra_photos_captions = FieldList(
			StringField(
			'Additional Photo Caption',
			default="No caption",
			validators=[Length(max=150)]))
	link_href = StringField(
			'If adding a relevant link which will fall below the Content section, copy complete HTTP URL here ( example: https://www.abolitionistlawcenter.org ):',
			validators=[URL(), Optional(), Length(max=150)])
	link_description = StringField(
			"Link Description ( example: \"Click Here for the Abolitionist Law Center\'s homepage\" ):", 
			validators=[Length(max=200)], default="Click Here")
	submit_new = SubmitField('Create Post')
	submit_update = SubmitField('Submit')