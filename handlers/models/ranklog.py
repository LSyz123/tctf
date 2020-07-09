from datetime import datetime

from handlers.models.base import BaseModel
from handlers.models.user import UserModel
from handlers.models.chanllage import ChanllageModel
from peewee import *


class RanklogModel(BaseModel):
    user = CharField(max_length=50, verbose_name='User')
    chanllage_id = IntegerField(verbose_name='赛题')
    chanllage = CharField(max_length=50, verbose_name='赛题名称')
    event = CharField(verbose_name='事件', max_length=255)
    answer = CharField(verbose_name='答案', max_length=255)
    uptime = DateTimeField(verbose_name='时间', default=datetime.now())
    rank = IntegerField(verbose_name='分数')

    @classmethod
    def extend(cls):
        return cls.select(cls, UserModel.id, UserModel.username, ChanllageModel.id).join(UserModel, ChanllageModel)

    class Meta:
        table_name = 'ranklog'
