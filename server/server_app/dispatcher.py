from .base_server import BaseServer
from .base_storage import BaseStorage
from  types import FunctionType
from .base_handler import Handler


class Dispatcher:
    def __init__(self, server: BaseServer, storage: BaseStorage) -> None:
        self.server = server
        self.storage = storage
    
    def registr_message_handler(self, handler: Handler):
        def decorator():
            handler
        return decorator