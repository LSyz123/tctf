from handlers.models.base import BaseModel
from handlers.models.user import UserModel

from peewee import *


class RankModel(BaseModel):
    user = ForeignKeyField(UserModel, verbose_name='User')
    rank = FloatField(verbose_name='Rank')

    class Meta:
        table_name = 'rank'
