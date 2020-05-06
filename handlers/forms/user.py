from wtforms_tornado import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(Form):
    username = StringField('username', validators=[
        DataRequired(message='Please input username'),
        Length(min=4, max=50, message='Invalid username')])
    password = PasswordField('password', validators=[
        DataRequired(message='Please input password'),
        Length(min=4, max=50, message='Invalid password')])
    password_check = PasswordField('password_check', validators=[
        DataRequired(message='Please input password_check'),
        EqualTo('password', message='Password must equal to password_check')])
    email = StringField('email',validators=[
        DataRequired(message='Please input email'),
        Email(message='Invalid email')])


class LoginForm(Form):
    username = StringField('Username', validators=[
        DataRequired(message='Please input username'),
        Length(min=4, max=50, message='Invalid username')])

    password = PasswordField('Password', validators=[
        DataRequired(message='Please input password_check'),
        EqualTo('password', message='Password must equal to password_check')])
