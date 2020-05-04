import peewee
import peewee_async

db = peewee_async.MySQLDatabase()


class BaseModel(peewee.Model):
    class Meta:
        db = None
