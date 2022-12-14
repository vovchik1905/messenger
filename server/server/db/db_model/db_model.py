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


class PrivateHash(BaseModel):
    """
    
    """
    password = CharField(null=True, default=None)
    
    class Meta:
        db_table = 'PrivateHashs'


class PrivateKey(BaseModel):
    """
    
    """
    key = CharField(null=True, default=None)
    
    class Meta:
        db_table = 'PrivateKeys'


class CryptoFunk(BaseModel):
    """
    
    """
    funk = CharField(null=True, default=None)

    class Meta:
        db_table = 'CryptoFunks'


class MessageContent(BaseModel):
    """
    
    """
    content = BlobField(null=True, default=None)
    content_type = CharField(null=True, default=None)
    content_date = DateField(null=True, default=None)
    content_time = TimeField(null=True, default=None)
    content_key = ForeignKeyField(PrivateKey)
    crypto_funk = ForeignKeyField(CryptoFunk)

    class Meta:
        db_table = 'MessageContents'


class User(BaseModel):
    """
    
    """
    username = CharField(null=True, default=None)
    create_date = DateField(null=True, default=None)
    create_time = TimeField(null=True, default=None)
    last_online_date = DateField(null=True, default=None)
    last_online_time = TimeField(null=True, default=None)
    private_info = ForeignKeyField(PrivateHash)

    class Meta:
        db_table = 'Users'


class Chat(BaseModel):
    """
    
    """
    creator_user = ForeignKeyField(User)
    create_date = DateField(null=True, default=None)
    create_time = TimeField(null=True, default=None)
    chat_name = CharField(null=True, default=None)

    class Meta:
        db_table = 'Chats'


class Message(BaseModel):
    """
    
    """
    creator_user_id = ForeignKeyField(User)
    #recipient_user_id = ForeignKeyField(User)
    create_date = DateField(null=True, default=None)
    create_time = TimeField(null=True, default=None)
    content_id = ForeignKeyField(MessageContent)

    class Meta:
        db_table = 'Messages'


class Chat_Message(BaseModel):
    """
    
    """
    chat_id = ForeignKeyField(Chat)
    message_id = ForeignKeyField(Message)
    
    class Meta:
        db_table = 'Chats_Messages'


class User_Chat(BaseModel):
    """
    
    """
    user_id = ForeignKeyField(User)
    chat_id = ForeignKeyField(Chat)

    class Meta:
        db_table = 'Users_Chats'