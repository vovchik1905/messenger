from server_app.base_server import BaseServer
from server_app.connection import Connection
from db.db_scripts.db_scripts import MessengerDataBase


class MessengerServer(BaseServer):
    async def send_text(self, user_id: int, text: str):
        connection = MessengerDataBase.get_connection_with_user_id(user_id)
        data = text.encode('ascii')
        return await super().send(connection, data)