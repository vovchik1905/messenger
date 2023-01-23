from local_objects import *
from state_class import state
from server.server.db.db_model.db_model import *
from server.server import *
from datetime import datetime
#from server.server_app.server_requests import send_request
from server.server_app.base_server import BaseServer


cmd_list = ('BACK', 'EXIT')

def Check_for_cmd(string)->bool:
    if string in cmd_list:
        return True
    else:
        return False

class cmd_func:
    def func0(users:user):
        if(users.state == state.state_names.index('WAIT_FOR_SELECT')):
            Connection.update(connection_end_datetime = datetime.now())
        return state.reverse_tree[users.state][0]
    def func1(users:user):
        return state.state_names.index('EXIT')

cmd = {'BACK':cmd_func.func0, 'EXIT':cmd_func.func1}

async def Choose_state(users:user, server:BaseServer,  conn:Connection = None)->int:
    if len(state.tree[users.state]) == 1:
        return state.tree[users.state][0]
    else:
        list = []
        for i in range(len(state.tree[users.state])):
            list.append(state.state_names[state.tree[users.state][i]])

        """"""#общение с клиентом
        str_list = " ".join(list)
        await server.send(conn, str_list)
        data_bytes = await server.__recive(conn)
        answer = data_bytes.decode()

        """"""

        if Check_for_cmd(answer): return cmd.get(answer)(users)
        if answer in list: return state.state_names.index(answer)
        else:
            await server.send(conn, "PRINT введенная команда не распознана, попробуйте еще раз")
            return users.state
