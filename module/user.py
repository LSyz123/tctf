import peewee


class UserModel(peewee.Model):
    username = peewee.CharField(max_length=255, verbose_name='用户名')
    password = peewee.CharField(max_length=255, verbose_name='密码')
    img = peewee.CharField(max_length=255, verbose_name='头像')
    email = peewee.CharField(max_length=255, verbose_name='邮箱')
    admin = peewee.BooleanField(default=False)

    class Meta:
        db_name = 'users'
