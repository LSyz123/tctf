from wtforms_tornado import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired, Length


class AnswerForm(Form):
    answer = StringField('answer', validators=[
        DataRequired(message='Please input answer'),
        Length(min=4, max=50, message='Invalid answer')])
