from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms import IntegerField
from wtforms import SelectField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class LinuxForYouForm(FlaskForm):
    """This form is used to take 3 pieces of information about a pdf,
    as well as the pdf itself for a magazine issue.
    """
    issue_number = SelectField(
            'Issue Number',
            choices=[(str(num), str(num)) for num in range(1, 100)],
            validators=[DataRequired()])
    year = SelectField(
            'Year',
            choices=[
            (str(year), str(year)) for year in range(2005, 2022)
            ],
            validators=[DataRequired()])
    month = SelectField('Month', 
                        choices=[
                        ('January', 'January'),
                        ('February', 'February'),
                        ('March', 'March'),
                        ('April', 'April'),
                        ('May', 'May'),
                        ('June', 'June'),
                        ('July', 'July'),
                        ('August', 'August'),
                        ('September', 'September'),
                        ('October', 'October'),
                        ('November', 'November'),
                        ('December', 'December')
                        ], validators=[DataRequired()])
    linux_for_you_pdf = FileField(
            'PDF File',
            validators=[DataRequired()])
    submit = SubmitField('Submit')