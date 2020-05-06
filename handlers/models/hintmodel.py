from handlers.models.base import BaseModel
from handlers.models.chanllage import ChanllageModel

from peewee import *


class HintModel(BaseModel):
    chanllage = ForeignKeyField(ChanllageModel)
    message = TextField(verbose_name='提示信息')
    sub_rank = IntegerField(verbose_name='消费分数')

    class Meta:
        table_name = 'hint'
