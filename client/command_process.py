import sys
PATH = "D:\pyton\messenger-1"
sys.path.append(PATH)

from state_class import state
from db_class import *
from request_class import *
from peewee import *
from server.server.db.db_model.db_model import *
from datetime import datetime


class func:
    def func0(users:user):
        Connection.create(host = users.connection_.host, port = users.connection_.port, connection_start_datetime = users.connection_.time)
    def func1(users:user):
        users.login = request.get('LOGIN')
        query = User.select().where(User.username == users.login)
        if query.exists(): return True
        else: return False
    def func2(users:user):
        users.login = request.get('LOGIN')
        query = User.select().where(User.username == users.login)
        if query.exists(): return False
        else: return True
    def func3(users:user):
        ID = User.get(User.id == users.id).private_info
        if PrivateHash.get(PrivateHash.id == ID).password == request.get('PASSWORD'): return True
        else: return False
    def func4(users:user):
        users.password = request.get('PASSWORD')
    def func5(users:user)->bool:
        if users.password == request.get('PASSWORD_REPEAT'): return True
        else: return False
    def func6(users:user):#пока пропущу потому что хз что здесь писать
        users.state = 8
    def func7(users:user):
        query = User_Chat.get(User_Chat.user_id == users.id).chat_id
        print("названия доступных чатов")
        for ID in query:
            print("{Chat.get(Chat.id == ID).chat_name}\n")
        Name = request.get('CHAT_SELECT')
        users.curr_chat = Chat.get(Chat.chat_name == Name).chat_id
    def func8(users:user):
        chat_name_ = request.get('CHAT_SELECT')
        user_name = request.get('CHAT_CREATE')
        second_user_id = User.get(User.username == user_name).id
        if second_user_id.exists():
            creation_date = datetime.date()
            creation_time = datetime.time() 
            created_chat = Chat.create(creator_user = users.id, create_date = creation_date,  create_time = creation_time, chat_name = chat_name_)
            User_Chat.create(user_id = users.id, chat_id = created_chat.id)
            User_Chat.create(user_id = second_user_id, chat_id = created_chat.id)
            
            return True
        else:
            print("такого пользователся не существует\n")
            return False

    def func9(users:user):#ждем
        users.state = 12
    def func10(users:user):#пока без подгрузки истории ибо ну его нахуй
        #query = Chat_Message.get(Chat_Message.chat_id == users.curr_chat).message_id
        #query_2 = Message.select().where(Message.id in query).order_by(Message.create_date).get().content.id
        return True
        
    def func11(users:user):
        message_ = request.get('TYPE_MESSAGE')
        #client.send(message)
        creation_date = datetime.date()
        creation_time = datetime.time()
        MessageContent.create(content = message_, content_date = creation_date, content_time = creation_time)

state_func = {'START':func.func0, 'LOGIN_IN':func.func1, 'LOGIN_UP':func.func2, 'PASS_IN':func.func3
            , 'PASS_UP':func.func4, 'PASS_REPEAT':func.func5, 'WAIT_FOR_SELECT':func.func6, 'SELECT_CHAT':func.func7
            , 'CREATE_CHAT':func.func8 , 'WAIT_IN_CHAT':func.func9, 'SEND_HISTORY':func.func10
            , 'SEND_MESSAGE':func.func11}

if __name__ == "__main__":
    connection1 = connection(1, 1, 1)
    User1 = user('arseny', 0, 1, 1, connection1)
    print(state_func.get(state.state_names[User1.state])(User1))
    #print(User1.state)
    #print(User.get(User.id == User1.id).private_info)

