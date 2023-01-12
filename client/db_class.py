        
class connection:
    def __init__(self, host, port, time):
        self.host = host
        self.port = port
        self.time = time

class user:
    def __init__(self, login, password, state, id, connection_:connection):
        self.login = login
        self.password = password
        self.state = state
        self.id = id
        self.connection_ = connection_
