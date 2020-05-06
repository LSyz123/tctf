from handlers.models.base import BaseModel
from handlers.models.chanllage import ChanllageModel

from peewee import *


class HintModel(BaseModel):
    chanllage = ForeignKeyField(ChanllageModel)
    message = TextField(verbose_name='Message')
    sub_rank = IntegerField(verbose_name='SubRank')

    class Meta:
        table_name = 'hint'
