from server.server.db.db_model.db_model import *

class request:
    def Get_id(table_name:BaseModel, condition):
        return table_name.get(condition)
    def Select(table_name:BaseModel, condition, arg):
        return table_name.select(arg).where(condition)
