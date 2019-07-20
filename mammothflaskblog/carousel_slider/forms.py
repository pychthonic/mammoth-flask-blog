from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import FileField
from wtforms import StringField
from wtforms.validators import Length
from wtforms.validators import DataRequired


class CarouselForm(FlaskForm):
    caption = StringField('Caption',
                          validators=[Length(max=500),
                          DataRequired()])
    image_file = FileField('Image')
    submit_new = SubmitField('Submit New')
    submit_update = SubmitField('Submit Update')