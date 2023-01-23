from __future__ import annotations
from server_app.base_server import BaseServer, Callback
from config import ServerConfig
from server_app.connection import Connection
from  types import FunctionType
from typing import Callable, Any
from server_app.server_state import ServerState


class DataFilters:
    def __init__(self) -> None:
        pass

    def get_data_filter(self) -> None:
        pass

    def set_data_filter(self) -> None:
        pass

def check_state(state):
    pass

def check_data_filter(data):
    pass

def registr_message_handler(callback_func: Callable[[BaseServer, Connection, bytes], Any],
                            server: BaseServer, data_filter: FunctionType, state: ServerState) -> None:
    callback = Callback(callback_func, data_filter, state)
    server.add_new_callback(callback)

def message_handler(state: ServerState = 1, data_filter: FunctionType = lambda data: True) -> Callable:
    def handler_decorator(callback_func: Callable[[BaseServer, Connection, bytes], Any]) -> Callable:
        def wrapped(server: BaseServer, conn: Connection = None, data: bytes = None, *args, **kwargs) -> Callable:
            registr_message_handler(callback_func, server, data_filter, state)
    
        return wrapped
    return handler_decorator

@message_handler(state=1)
async def callback_f1(server: BaseServer, conn: Connection = None, data: bytes = None):
    user_data =  data.decode()
    if user_data == "vovik":
        output_data = "$$$$$$"
        await server.send(conn, output_data.encode('ascii'))
    else:
        await server.send(conn, data.upper())

def start_messenger():
    server = BaseServer(ServerConfig.SERVER_HOST,
                        ServerConfig.SERVER_PORT,
                        ServerConfig.SERVER_CONNECTIONS_NUM)
    
    callback_f1(server)
    server.start()

if __name__ == "__main__":
    start_messenger()