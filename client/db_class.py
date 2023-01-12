class user:
    def __init__(self, name, password, state, id):
        self.name = name
        self.password = password
        self.state = state
        self.id = id
        
class connection:
    def __init__(self, host, port, time):
        self.host = host
        self.port =  port
        self.time = time
