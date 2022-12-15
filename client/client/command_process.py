from state_class import state
from user_class import user
from psycopg2 import OperationalError

class func:
    def func0(User:user):
            User.state = 0
    def func1(User:user):
            User.state = 1
    def func2(User:user):
            User.state = 2
    def func3(User:user):
            User.state = 3
    def func4(User:user):
            User.state = 4
    def func5(User:user):
            User.state = 5
    def func6(User:user):
            User.state = 6
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
User1 = user('Alex', 0, 10)
state_func.get(state.state_names[User1.state])(User1)
print(User1.state)
