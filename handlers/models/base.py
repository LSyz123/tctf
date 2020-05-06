import peewee
from setting import db


class BaseModel(peewee.Model):
    class Meta:
        database = db
