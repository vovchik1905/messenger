from ..db_model.db_model import *


"""Singlton pattern (with metaclass) start:"""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
"""Singlton pattern end."""

class MessagerDataBase(metaclass=Singleton):
    """
    
    """
    def __init__(self, db) -> None:
        self.db = db

    def create_db(self, db_config) -> bool:
        pass

    def create_tables(self) -> bool:
        with self.db:
            self.db.create_tables(PrivateHash, PrivateKey,
                                    CryptoFunk, Connection,
                                    MessageContent, User,
                                    Chat, Message,
                                    User_Chat, Chat_Message,
                                    User_Connection)

    def setting_up_tables(self) -> bool:
        pass