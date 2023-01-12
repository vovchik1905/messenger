from state_class import state
from db_class import *
from request_class import *
from peewee import *
from ..server.server.db.db_model.db_model import *


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
    def func7(User:user):
        User.state = 7
    def func8(User:user):
        User.state = 8
    def func9(User:user):
        User.state = 9
    def func10(User:user):
        User.state = 10
    def func11(User:user):
        User.state = 11
    def func12(User:user):
        User.state = 12
    def func13(User:user):
        User.state = 13
    def func14(User:user):
        User.state = 14
    def func15(User:user):
        User.state = 15

state_func = {'START':func.func0, 'SING_IN':func.func1, 'SING_UP':func.func2, 'LOGIN_IN':func.func3, 'LOGIN_UP':func.func4
            , 'PASS_UP':func.func5, 'PASS_REPEAT':func.func6, 'PASS_IN':func.func7, 'WAIT_FOR_SELECT':func.func8, 'SELECT_CHAT':func.func9
            , 'CREATE_CHAT':func.func10 ,'SELECT_USER':func.func11, 'WAIT_IN_CHAT':func.func12, 'SEND_HISTORY':func.func13
            , 'SEND_MESSAGE':func.func14, 'GET_MESSAGE':func.func15}

if __name__ == "__main__":
        User1 = user('Alex', 0, 0, 10)
        state_func.get(state.state_names[User1.state])(User1)
        print(User1.state)
