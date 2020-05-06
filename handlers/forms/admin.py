from wtforms_tornado import Form
from wtforms.fields import StringField, PasswordField, FileField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, Length


class AddUserForm(Form):
    username = StringField('username', validators=[
        DataRequired(message='用户名不能为空'),
        Length(min=4, max=50, message='用户名长度不合格（4-50）')])
    password = PasswordField('password', validators=[
        DataRequired(message='密码不能为空'),
        Length(min=4, max=50, message='无效的密码长度（4-50）')])
    email = StringField('email', validators=[
        DataRequired(message='邮箱不能为空'),
        Email(message='无效的邮箱')])


class AddChanllageForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='名称不能为空'),
        Length(min=1, max=50, message='名称长度不合格（1-50）')])
    type_name = StringField('type_name', validators=[
        DataRequired(message='类型不能为空')])
    describe = StringField('describe', validators=[
        DataRequired(message='描述不能为空'),
        Length(min=1, max=255, message='描述长度不合格（1-50）')])
    rank = IntegerField('rank', validators=[
        DataRequired(message='分数不能为空')])
    low = IntegerField('low', validators=[
        DataRequired(message='最低分不能为空')])
    people = IntegerField('people', validators=[
        DataRequired(message='分数递减人数不能为空')])
    answer = StringField('answer', validators=[
        DataRequired(message='答案不能为空'),
        Length(min=1, max=255, message='答案长度不合格（1-255）')])
    upload_file = FileField('upload_file')
    link = StringField('link')


class UpdateChanllageForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='名称不能为空'),
        Length(min=1, max=50, message='名称长度不合格（1-50）')])
    describe = StringField('describe', validators=[
        DataRequired(message='描述不能为空'),
        Length(min=1, max=255, message='描述长度不合格（1-50）')])
    rank = IntegerField('rank', validators=[
        DataRequired(message='分数不能为空')])
    low = IntegerField('low', validators=[
        DataRequired(message='最低分不能为空')])
    people = IntegerField('people', validators=[
        DataRequired(message='分数递减人数不能为空')])
    answer = StringField('answer', validators=[
        DataRequired(message='答案不能为空'),
        Length(min=1, max=255, message='答案长度不合格（1-255）')])
    link = StringField('link')


class AddNewsForm(Form):
    message = StringField('message', validators=[
        DataRequired(message='公告不能为空'),
        Length(min=4, max=50, message='公告长度不合格（1-50）')])


class SystemForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='系统名称不能为空'),
        Length(min=4, max=50, message='系统名称长度不合格（4-50）')])
    game_mode = BooleanField('game_mode', validators=[
        DataRequired(message='比赛模式不能为空')])
    start = DateField('start', validators=[DataRequired(message='请输入开始时间')])
    end = DateField('end', validators=[DataRequired(message='请输入结束时间')])


class AddHintForm(Form):
    chanllage = StringField('chanllage', validators=[
        DataRequired(message='赛题不能为空')])
    message = StringField('message', validators=[
        DataRequired(message='提示信息不能为空')])
    sub_rank = IntegerField('sub_rank', validators=[
        DataRequired(message='消费分数不能为空')])


class AddTypeForm(Form):
    name = StringField('name', validators=[
        DataRequired(message='类型名不能为空')])
