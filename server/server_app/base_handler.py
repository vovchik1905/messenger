from __future__ import annotations
from .connection import Connection
from .base_server import BaseServer
from .base_storage import BaseStorage
from  types import FunctionType


class Handler:
    def __init__(self, server: BaseServer, connection: Connection, data: bytes, callback: FunctionType = None) -> None:
        self.server = server
        self.conn = connection
        self.data = data
        self.callback = callback

    async def register(self):
        await self.callback
        await self.server.send(self.conn, self.data.upper())
    
    @classmethod
    def create(cls, server: BaseServer, connection: Connection, data: bytes, callback: FunctionType = None) -> None:
        pass