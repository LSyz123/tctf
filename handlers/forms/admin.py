from wtforms_tornado import Form
from wtforms.fields import StringField, PasswordField, FileField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, Length


class AddUserForm(Form):
    username = StringField('username', validators=[
        DataRequired(message='Please input username'),
        Length(min=4, max=50, message='Invalid username')])
    password = PasswordField('password', validators=[
        DataRequired(message='Please input password'),
        Length(min=4, max=50, message='Invalid password')])
    email = StringField('email', validators=[
        DataRequired(message='Please input email'),
        Email(message='Invalid email')])


class AddChanllageForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='Please input name'),
        Length(min=4, max=50, message='Invalid name')])
    type_name = StringField('type_name', validators=[
        DataRequired(message='Please input name')])
    describe = StringField('describe', validators=[
        DataRequired(message='Please input describe'),
        Length(min=4, max=255, message='Invalid describe')])
    rank = IntegerField('rank', validators=[
        DataRequired(message='Please input rank')])
    low = IntegerField('low', validators=[
        DataRequired(message='Please input low')])
    people = IntegerField('people', validators=[
        DataRequired(message='Please input people')])
    answer = StringField('answer', validators=[
        DataRequired(message='Please input answer'),
        Length(min=4, max=255, message='Invalid answer')])
    upload_file = FileField('upload_file', validators=[])
    link = StringField('name', validators=[
        DataRequired(message='Please input link'),
        Length(min=4, max=50, message='Invalid link')])


class UpdateChanllageForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='Please input name'),
        Length(min=4, max=50, message='Invalid name')])
    describe = StringField('describe', validators=[
        DataRequired(message='Please input describe'),
        Length(min=4, max=255, message='Invalid describe')])
    rank = IntegerField('rank', validators=[
        DataRequired(message='Please input rank')])
    low = IntegerField('low', validators=[
        DataRequired(message='Please input low')])
    people = IntegerField('people', validators=[
        DataRequired(message='Please input people')])
    answer = StringField('answer', validators=[
        DataRequired(message='Please input answer'),
        Length(min=4, max=255, message='Invalid answer')])
    link = StringField('name', validators=[
        DataRequired(message='Please input link'),
        Length(min=4, max=50, message='Invalid link')])


class AddNewsForm(Form):
    message = StringField('message', validators=[
        DataRequired(message='Please input message'),
        Length(min=4, max=50, message='Invalid message')])


class SystemForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='Please input name'),
        Length(min=4, max=50, message='Invalid name')])
    game_mode = BooleanField('game_mode', validators=[
        DataRequired(message='Please input game_mode'),
        Length(min=4, max=50, message='Invalid game_mode')])
    start = DateField('start', validators=[DataRequired(message='Please input start')])
    end = DateField('end', validators=[DataRequired(message='Please input end')])


class AddHintForm(Form):
    chanllage = StringField('chanllage', validators=[
        DataRequired(message='Please input chanllage'),
        Length(min=4, max=50, message='Invalid chanllage')])
    message = StringField('message', validators=[
        DataRequired(message='Please input message'),
        Length(min=4, max=50, message='Invalid message')])
    sub_rank = IntegerField('sub_rank', validators=[
        DataRequired(message='Please input sub_rank')])


class AddTypeForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='Please input name')])
