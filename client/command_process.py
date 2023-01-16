import sys
PATH = "D:\pyton\messenger-1"
sys.path.append(PATH)

from state_class import state
from db_class import *
from request_class import *
from peewee import *
from server.server.db.db_model.db_model import *


class func:
    def func0(users:user):
        Connection.create(host = users.connection_.host, port = users.connection_.port, connection_start_datetime = users.connection_.time)
    def func1(users:user)->bool:
        query = User.select().where(User.username == users.login)
        if query.exists(): return True
        else: return False
    def func2(users:user)->bool:
        query = User.select().where(User.username == users.login)
        if query.exists(): return True
        else: return False
    def func3(users:user):
        users.login = request.get('LOGIN')
    def func4(users:user):
        users.login = request.get('LOGIN')
    def func5(users:user):
        users.password = request.get('PASSWORD')
    def func6(users:user)->bool:
        if users.password == request.get('PASSWORD_REPEAT'): return True
        else: return False
    def func7(users:user):
        ID = User.get(User.id == users.id).private_info
        if PrivateHash.get(PrivateHash.id == ID).password == request.get('PASSWORD'): return True
        else: return False
    def func8(users:user):#пока пропущу потому что хз что здесь писать
        users.state = 8
    def func9(users:user):
        
        request.get('CHAT_SELECT')
    def func10(users:user):
        users.state = 10
    def func11(users:user):
        users.state = 11
    def func12(users:user):
        users.state = 12
    def func13(users:user):
        users.state = 13
    def func14(users:user):
        users.state = 14
    def func15(users:user):
        users.state = 15

state_func = {'START':func.func0, 'SING_IN':func.func1, 'SING_UP':func.func2, 'LOGIN_IN':func.func3, 'LOGIN_UP':func.func4
            , 'PASS_UP':func.func5, 'PASS_REPEAT':func.func6, 'PASS_IN':func.func7, 'WAIT_FOR_SELECT':func.func8, 'SELECT_CHAT':func.func9
            , 'CREATE_CHAT':func.func10 ,'SELECT_USER':func.func11, 'WAIT_IN_CHAT':func.func12, 'SEND_HISTORY':func.func13
            , 'SEND_MESSAGE':func.func14, 'GET_MESSAGE':func.func15}

if __name__ == "__main__":
    connection1 = connection(1, 1, 1)
    User1 = user('arseny', 0, 1, 1, connection1)
    print(state_func.get(state.state_names[User1.state])(User1))
    #print(User1.state)
    #print(User.get(User.id == User1.id).private_info)

