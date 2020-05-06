from handlers.models.base import BaseModel
from peewee import *
from datetime import datetime


class MessageModel(BaseModel):
    message = TextField(verbose_name='公告')
    add_time = DateField(verbose_name='添加时间', default=datetime.now())

    class Meta:
        table_name = 'message'
