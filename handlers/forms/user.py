from wtforms_tornado import Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(Form):
    username = StringField('username', validators=[
        DataRequired(message='请输入用户名'),
        Length(min=4, max=50, message='用户名长度不合格（4-50）')])
    password = PasswordField('password', validators=[
        DataRequired(message='请输入密码'),
        Length(min=4, max=50, message='Invalid password')])
    password_check = PasswordField('password_check', validators=[
        DataRequired(message='请再次输入密码'),
        EqualTo('password', message='两次输入的密码不相同')])
    email = StringField('email',validators=[
        DataRequired(message='请输入邮箱'),
        Email(message='不合格的邮箱')])


class LoginForm(Form):
    username = StringField('Username', validators=[
        DataRequired(message='请输入用户名')])

    password = PasswordField('Password', validators=[
        DataRequired(message='请输入密码')])
