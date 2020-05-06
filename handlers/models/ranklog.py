from datetime import datetime

from handlers.models.base import BaseModel
from handlers.models.user import UserModel
from handlers.models.chanllage import ChanllageModel
from peewee import *


class RanklogModel(BaseModel):
    user = ForeignKeyField(UserModel, verbose_name='用户')
    chanllage = ForeignKeyField(ChanllageModel, verbose_name='赛题')
    event = CharField(verbose_name='事件', max_length=255)
    answer = CharField(verbose_name='答案', max_length=255)
    uptime = DateTimeField(verbose_name='时间', default=datetime.now())
    rank = IntegerField(verbose_name='分数')

    class Meta:
        table_name = 'flaglog'
