from handlers.models.base import BaseModel

from peewee import *


class SystemModel(BaseModel):
    name = CharField(max_length=255, verbose_name='系统名称')
    game_mode = BooleanField(verbose_name='比赛模式', default=False)
    start = DateTimeField(verbose_name='开始时间')
    end = DateTimeField(verbose_name='结束时间')

    class Meta:
        table_name = 'system'
