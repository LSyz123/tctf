from handlers.models.base import BaseModel
from handlers.models.type import TypeModel
from peewee import *


class ChanllageModel(BaseModel):
    name = CharField(max_length=50, verbose_name='赛题名称')
    type_name = ForeignKeyField(TypeModel, verbose_name='赛题类型')
    describe = CharField(max_length=255, verbose_name='描述')
    rank = IntegerField(verbose_name='分数')
    low = IntegerField(verbose_name='最低分')
    people = IntegerField(verbose_name='分数递减人数')
    answer = CharField(max_length=255, verbose_name='答案')
    file = CharField(max_length=255, verbose_name='赛题文件')
    link = CharField(max_length=255, verbose_name='赛题链接')

    class Meta:
        table_name = 'chanllage'
