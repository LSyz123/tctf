import peewee
import peewee_async

db = peewee_async.MySQLDatabase('CTF', host='127.0.0.1', port=3306, user='root', password='WhoAmI123')


class BaseModel(peewee.Model):
    class Meta:
        database = db
