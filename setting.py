import peewee_async
import os

settings = {
    'secret_key': 'ZGGA#Mp4yL4w5CDu',
    'secret_algorithm': 'HS256',
    'jwt_expire': 24*3600,
    'UPLOAD_BASE': os.path.join(os.path.dirname(__file__), "static/uploads/"),
}

db = peewee_async.MySQLDatabase('CTF', host='127.0.0.1', port=3306, user='root', password='WhoAmI123', charset='utf8')
