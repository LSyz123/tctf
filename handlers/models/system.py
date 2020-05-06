from handlers.models.base import BaseModel

from peewee import *


class SystemModel(BaseModel):
    name = CharField(max_length=255, verbose_name='name')
    game_mode = BooleanField(verbose_name='Game mode', default=False)
    start = DateField(verbose_name='Start time')
    end = DateField(verbose_name='End time')

    class Meta:
        table_name = 'system'
