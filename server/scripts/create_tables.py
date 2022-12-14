import sys
sys.path.append("D:\HSE\прога\project3\messenger")
from server.server.db.db_scripts.db_scripts import MessagerDataBase
from server.server.db.db_model.db_model import db


def create_db_tables() -> None:
    """
    
    """
    simple_messager_data_base = MessagerDataBase(db)
    simple_messager_data_base.create_tables()


if __name__ == "__main__":
    create_db_tables()