from handlers.models.base import BaseModel
from peewee import *
from bcrypt import hashpw, gensalt


class PasswordHash(bytes):
    def check_password(self, password):
        password = password.encode('utf-8')
        return hashpw(password, self) == self


class PasswordField(BlobField):
    def __init__(self, iterations=12, *args, **kwargs):
        if None in (hashpw, gensalt):
            raise ValueError('Missing library required for PasswordField: bcrypt')
        self.bcrypt_iterations = iterations
        self.raw_password = None
        super(PasswordField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        """Convert the python value for storage in the database."""
        if isinstance(value, PasswordHash):
            return bytes(value)

        if isinstance(value, str):
            value = value.encode('utf-8')
        salt = gensalt(self.bcrypt_iterations)
        return value if value is None else hashpw(value, salt)

    def python_value(self, value):
        """Convert the database value to a pythonic value."""
        if isinstance(value, str):
            value = value.encode('utf-8')

        return PasswordHash(value)


class UserModel(BaseModel):
    username = CharField(max_length=50, verbose_name='Username')
    password = PasswordField(verbose_name='Password')
    email = CharField(max_length=50, verbose_name='Email')
    admin = BooleanField(verbose_name='Admin', default=False)
    rank = IntegerField(verbose_name='Rank', default=0)

    class Meta:
        table_name = 'users'

