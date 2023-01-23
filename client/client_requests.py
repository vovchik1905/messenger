from server.server.db.db_model.db_model import *
from server.server_app.base_server import BaseServer

class request:
    #def Get_id(table_name:BaseModel, condition):
    #    return table_name.get(condition)
    #def Select(table_name:BaseModel, condition, arg):
    #    return table_name.select(arg).where(condition)
    def client_input_request(data):
        print(data)
        
