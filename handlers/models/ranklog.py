from datetime import datetime

from handlers.models.base import BaseModel
from handlers.models.user import UserModel
from handlers.models.chanllage import ChanllageModel
from peewee import *


class RanklogModel(BaseModel):
    user = ForeignKeyField(UserModel, verbose_name='User')
    chanllage = ForeignKeyField(ChanllageModel, verbose_name='Chanllage')
    event = CharField(verbose_name='Event', max_length=255)
    answer = CharField(verbose_name='Flag', max_length=255)
    uptime = DateTimeField(verbose_name='Upload time', default=datetime.now())
    rank = IntegerField(verbose_name='Rank')

    class Meta:
        table_name = 'flaglog'
