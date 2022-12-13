from peewee import *
from ....settings.private.db_config import DbConfig



db = PostgresqlDatabase(database=DbConfig.DATABAZE,
                        user=DbConfig.USER,
                        password=DbConfig.PASSWORD,
                        host=DbConfig.HOST,
                        port=DbConfig.PORT)


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order = 'id'


class PrivateHashs(BaseModel):
    password = CharField(null=True, default=None)
    
    class Meta:
        pass


class User(BaseModel):
    username = CharField(null=True, default=None)
    create_date = DateField(null=True, default=None)
    create_time = TimeField(null=True, default=None)
    last_online_date = DateField(null=True, default=None)
    last_online_time = TimeField(null=True, default=None)
    private_info = ForeignKeyField(PrivateHashs)

    class Meta:
        pass


class Message(BaseModel):
    creator_user = ForeignKeyField(User)
    recipient_user = ForeignKeyField(User)
    create_date = DateField(null=True, default=None)
    create_time = TimeField(null=True, default=None)