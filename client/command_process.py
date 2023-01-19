import sys
PATH = "D:\pyton\messenger-1"
sys.path.append(PATH)

from state_class import *
from db_class import *
from request_class import *
from peewee import *
from server.server.db.db_model.db_model import *
from datetime import datetime


class func:
    def func0(users:user):
        users.state = Choose_state(users)
        Connection.create(host = users.connection_.host, port = users.connection_.port, connection_start_datetime = datetime.time)
        
    def func1(users:user):
        users.login = request.get('LOGIN')
        query = User.select().where(User.username == users.login)
        if query.exists(): users.state = Choose_state(users)
        else: print("введен неверный логин, попробуйте еще раз")

    def func2(users:user):
        users.login = request.get('LOGIN')
        query = User.select().where(User.username == users.login)
        if query.exists(): 
            print("пользователь с таким логином уже существует\nпопробуйте ввести другой логин")
        else: users.state = Choose_state(users)

    def func3(users:user):
        ID = User.get(User.id == users.id).private_info
        if PrivateHash.get(PrivateHash.id == ID).password == request.get('PASSWORD'): users.state = Choose_state(users)
        else: print("введен неверный пароль")

    def func4(users:user):
        users.password = request.get('PASSWORD')
        users.state = Choose_state(users)

    def func5(users:user):
        if users.password == request.get('PASSWORD_REPEAT'): users.state = Choose_state(users)
        else: print("введенные пароль не совпадают")

    def func6(users:user):#ждем
        users.state = Choose_state(users)

    def func7(users:user):
        query = User_Chat.get(User_Chat.user_id == users.id).chat_id
        print("названия доступных чатов")
        for ID in query:
            print(Chat.get(Chat.id == ID).chat_name)
        Name = request.get('CHAT_SELECT')
        input_chat_id = Chat.get(Chat.chat_name == Name).chat_id
        if input_chat_id is not None:
            users.curr_chat = input_chat_id
            users.state = Choose_state(users)
        else:
            print("введено неверное название чата")

    def func8(users:user):
        user_name = request.get('CHAT_CREATE')
        chat_name_ = request.get('CHAT_SELECT')
        second_user_id = User.get(User.username == user_name).id
        if second_user_id.exists():
            creation_date = datetime.date()
            creation_time = datetime.time() 
            created_chat = Chat.create(creator_user = users.id, create_date = creation_date,  create_time = creation_time, chat_name = chat_name_)
            User_Chat.create(user_id = users.id, chat_id = created_chat.id)
            User_Chat.create(user_id = second_user_id, chat_id = created_chat.id)
            
            users.state = Choose_state(users)
        else:
            print("пользователь, которого вы хотите добавить в чат ,не найден")

    def func9(users:user):#ждем
        users.state = Choose_state(users)

    def func10(users:user):#пока без подгрузки истории
        #query = Chat_Message.get(Chat_Message.chat_id == users.curr_chat).message_id
        #query_2 = Message.select().where(Message.id in query).order_by(Message.create_date).get().content.id
        print("подгрузка сообщений пока не доступна")
        users.state = Choose_state(users)
        
    def func11(users:user):
        message_ = request.get('TYPE_MESSAGE')
        creation_date = datetime.date()
        creation_time = datetime.time()
        MessageContent.create(content = message_, content_date = creation_date, content_time = creation_time)
        users.state = Choose_state(users)


state_func = {'START':func.func0, 'LOGIN_IN':func.func1, 'LOGIN_UP':func.func2, 'PASS_IN':func.func3
            , 'PASS_UP':func.func4, 'PASS_REPEAT':func.func5, 'WAIT_FOR_SELECT':func.func6, 'SELECT_CHAT':func.func7
            , 'CREATE_CHAT':func.func8 , 'WAIT_IN_CHAT':func.func9, 'SEND_HISTORY':func.func10
            , 'SEND_MESSAGE':func.func11}

if __name__ == "__main__":
    #connection1 = connection(1, 1, 1)
    #User1 = user('arseny', 0, 1, 1, connection1)
    #print(state_func.get(state.state_names[User1.state])(User1))
    #print(User1.state)
    #print(User.get(User.id == User1.id).private_info)
    print('0')
