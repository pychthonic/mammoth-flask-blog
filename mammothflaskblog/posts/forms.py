from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, MultipleFileField, FieldList
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(max=100)])
	content = TextAreaField('Content (Note: No links in Content section!)', validators=[DataRequired(), Length(max=25000)])
	main_photo = FileField('Main Photo')
	main_photo_caption = StringField('Main Photo Caption', validators=[Length(max=150)])
	extra_photos = MultipleFileField('Additional Photos', default=None)
	extra_photos_captions = FieldList(StringField('Additional Photo Caption', default="No caption", validators=[Length(max=150)]))
	link_href = StringField('If adding a relevant link which will fall below the Content section, copy complete HTTP URL here ( example: https://www.abolitionistlawcenter.org ):', validators=[Length(max=150)])
	link_description = StringField(
								"Link Description ( example: \"Click Here for the Abolitionist Law Center\'s homepage\" ):", 
								default="Click Here")
	submit_new = SubmitField('Create Post')
	submit_update = SubmitField('Submit')


