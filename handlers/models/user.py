from handlers.models.base import BaseModel
from peewee import *


class UserModel(BaseModel):
    id = IntegerField(verbose_name='ID', primary_key=True)
    username = CharField(max_length=50, verbose_name='Username')
    password = CharField(max_length=255, verbose_name='Password')
    email = CharField(max_length=50, verbose_name='Email')
    photo = CharField(max_length=255, verbose_name='Photo')
    admin = BooleanField(verbose_name='Admin')

    class Meta:
        table_name = 'users'


if __name__ == '__main__':
    db.create_tables([UserModel])
