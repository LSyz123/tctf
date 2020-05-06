from handlers.models.base import BaseModel
from handlers.models.type import TypeModel
from peewee import *


class ChanllageModel(BaseModel):
    name = CharField(max_length=50, verbose_name='Chanllage name')
    type_name = ForeignKeyField(TypeModel, verbose_name='Type name')
    describe = CharField(max_length=255, verbose_name='Describe')
    rank = IntegerField(verbose_name='Rank')
    low = IntegerField(verbose_name='Low')
    people = IntegerField(verbose_name='People')
    answer = CharField(max_length=255, verbose_name='Answer')
    file = CharField(max_length=255, verbose_name='File')
    link = CharField(max_length=255, verbose_name='Download link')

    class Meta:
        table_name = 'chanllage'
