from handlers.models.base import BaseModel
from peewee import *
from datetime import datetime


class MessageModel(BaseModel):
    message = TextField(verbose_name='messagebox')
    add_time = DateField(verbose_name='add time', default=datetime.now())

    class Meta:
        table_name = 'message'
