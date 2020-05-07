from datetime import datetime

from handlers.models.base import BaseModel

from peewee import *

from handlers.models.hint import HintModel
from handlers.models.user import UserModel


class BuylogModel(BaseModel):
    user = ForeignKeyField(UserModel, verbose_name='User')
    hint = ForeignKeyField(HintModel, verbose_name='Hint')
    time = DateTimeField(verbose_name='Buy time', default=datetime.now())
    rank = IntegerField(verbose_name='Rank')

    class Meta:
        table_name = 'buylog'
