from datetime import datetime

from handlers.models.base import BaseModel

from peewee import *


class BuylogModel(BaseModel):
    user = CharField(max_length=50, verbose_name='User')
    hint = TextField(verbose_name='提示信息')
    time = DateTimeField(verbose_name='Buy time', default=datetime.now())
    rank = IntegerField(verbose_name='Rank')

    class Meta:
        table_name = 'buylog'
