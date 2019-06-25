from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FileField
from wtforms.validators import Length, DataRequired


class CarouselForm(FlaskForm):
	caption = StringField('Caption', validators=[Length(max=500), DataRequired()])
	image_file = FileField('Image')
	submit_new = SubmitField('Submit New')
	submit_update = SubmitField('Submit Update')