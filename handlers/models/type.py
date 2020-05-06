from handlers.models.base import BaseModel
from peewee import *


class TypeModel(BaseModel):
    name = CharField(max_length=50, verbose_name='赛题类型')

    class Meta:
        table_name = 'type'
