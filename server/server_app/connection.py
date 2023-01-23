import socket
from .server_state import ServerState


class Connection():
    def __init__(self, socket: socket.socket, address: tuple, state: ServerState = None) -> None:
        self.socket = socket
        self.address = address
        #self.state = state