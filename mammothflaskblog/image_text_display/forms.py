from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, FileField
from wtforms.validators import Length


class TextAndImageForm(FlaskForm):
	text_part = TextAreaField('Text', validators=[Length(max=50000)])
	image_file = FileField('Image')
	submit_new = SubmitField('Submit New')
	submit_update = SubmitField('Submit Update')