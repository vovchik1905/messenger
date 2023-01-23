from __future__ import annotations
from  types import FunctionType
import asyncio
import socket
from .connection import Connection
from server_app.server_state import ServerState

class Callback:
    def __init__(self, callback_action: FunctionType,
                data_filter: FunctionType = lambda data: True,
                state: ServerState = None) -> None:
        self.callback_action = callback_action
        self.data_filter = data_filter
        self.state = state


class BaseServer():
    """
    Base Server class.
    """

    #CALLBACK_LIST = []

    def __init__(self, host: str, port: int, connections_num: int, callbacks: list[Callback] = []) -> None:
        """
        Init BaseServer object.

        Args:
            host (str): Server host
            port (int): Server port
            connections_num (int): Server num of connections in queue.
            callbacks (list[FunctionType], optional): list of callback funcs. Defaults to [].
        """
        self.host = host
        self.port = port
        self.connections_num = connections_num
        self.callbacks = callbacks
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((host, port))
        self.connections = set()
    
    def __check_new_connection(self, connection: Connection) -> bool:
        """
        Check new connection.

        Args:
            connection (Connection): Connection object

        Returns:
            bool: if new connection -> True else False 
        """
        if connection in self.connections:
            return False
        return True
    
    @property
    async def __accept(self) -> Connection | None:
        """
        Accept new connection.

        Returns:
            Connection | None: Connection object.
        """
        loop = asyncio.get_event_loop()                                     #получение текущего цикла событий
        new_connection = Connection(*await loop.sock_accept(self.server_socket))
        socket, addr = new_connection.socket, new_connection.address
        if self.__check_new_connection(socket):
            self.connections.add(new_connection)
            return new_connection
        return None
    
    async def __recive(self, connection: Connection) -> bytes:
        """
        Recive new data.

        Args:
            connection (Connection): _description_

        Returns:
            bytes | None: recive data
        """
        client_sock, client_addr = connection.socket, connection.address
        loop = asyncio.get_event_loop()
        try:
            data = await loop.sock_recv(client_sock, 4096)
            return data
        except ConnectionError:
            print(f"Client suddenly closed while receiving from {client_addr}")
            client_sock.close()
            self.connections.discard(connection)
            return None

    async def __sendall(self, connection: Connection, data: bytes) -> bool:
        """
        Sendall private method.

        Args:
            connection (Connection): _description_
            data (bytes): _description_

        Returns:
            bool: alrigt sendall/ not alrright sendall status
        """
        client_sock, client_addr = connection.socket, connection.address
        loop = asyncio.get_event_loop()
        try:
            await loop.sock_sendall(client_sock, data)
            return True
        except ConnectionError:
            print(f"Client suddenly closed, cannot send to {client_addr}")
            client_sock.close()
            self.connections.discard(connection)
            return False
    
    async def send(self, connection: Connection, data):
        """
        Send method.

        Args:
            connection (Connection): _description_
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        send_data = data
        return await self.__sendall(connection, send_data)

    async def handle_connection(self, connection: Connection) -> None:
        """
        Обработчик соединения, в бесконечном цикле принимает updates,
        а затем для каждого update создает таску в событийном цикле
        для каждой callback функции.

        Args:
            connection (Connection): Connection object.
        """
        loop = asyncio.get_event_loop()
        while True:
            recive_data = await self.__recive(connection)
            if recive_data is None or not recive_data:
                print("Disconnected by", connection.address)
                break
            for callback in self.callbacks:
                if callback.data_filter(recive_data) and callback.state == 1:
                    loop.create_task(callback.callback_action(self, connection, recive_data))

    @property
    async def run(self) -> None:
        """
        Метод объекта, запускает объект сервера,
        в бесконечном цикле обрабатывает новые
        подключения, а затем передает обработку
        подключения методу self.handle_connection().
        """
        self.server_socket.listen(self.connections_num)
        loop = asyncio.get_event_loop()                                     #получение текущего цикла событий
        while True:
            new_connection = await self.__accept
            if new_connection is not None:
                print(f"New connection: {new_connection.address}")
                loop.create_task(self.handle_connection(new_connection))
    
    def start(self) -> BaseServer:
        """
        Метод запускает сервер.
        Cоздаётся асинхронный цикл
        событий с корутиной self.run()

        Returns:
            BaseServer: object
        """
        asyncio.run(self.run)
        return self
    
    def add_new_callback(self, callback: Callback) -> None:
        """
        Add new callback handler.
        Args:
            callback (FunctionType): callback handler func
        """
        self.callbacks.append(callback)
    
    @staticmethod
    def check():
        pass