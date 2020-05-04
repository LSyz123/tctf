from wtforms import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(Form):
    username = StringField('Username', validators=(DataRequired(message='Please input username'), Length(min=4, max=50, message='Invalid username')))
    password = PasswordField('Password', validators=(DataRequired(message='Please input password'), Length(min=4, max=50, message='Invalid password')))
    email = StringField('Email', validators=(DataRequired(message='Please input email'), Email(message='Invalid email')))
    photo = StringField('photo')
