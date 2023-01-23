import sys
PATH = "D:\pyton\messenger-1"
sys.path.append(PATH)

from state_class import *
from local_objects import *
from input_functions import *
from peewee import *
from server.server.db.db_model.db_model import *
from server.server_app.base_server import BaseServer
from datetime import datetime
from color_print import *
from client.cmd import *


class func:
    def func0(users:user)->state:#ожидание/начало дерева
        return Choose_state(users)
        #Connection.create(host = users.connection_.host, port = users.connection_.port, connection_start_datetime = datetime.now())
        
    async def func1(users:user)->state:#login while sing in

        answer = input_template("логин")
        if Check_for_cmd(answer): return cmd.get(answer)(users)
        users.login = answer

        user_row = User.select().where(User.username == users.login)

        if user_row.exists():
            users.id = user_row.get().id 

            """"""
            return await Choose_state(users)
            """"""

        else: 
            red_text("введен неверный логин, попробуйте еще раз")
            return users.state

    async def func2(users:user)->state:#create login

        answer = input_template("логин")
        if Check_for_cmd(answer): 
            return cmd.get(answer)(users)
        users.login = answer

        query = User.select().where(User.username == users.login)

        if query.exists(): 
            red_text("пользователь с таким логином уже существует\nпопробуйте ввести другой логин")
            return users.state
        else: return Choose_state(users)

    async def func3(users:user)->state:#password input while sing in

        """"""
        user_id = User.select().where(User.username == users.login).get().id
        password_id = User.select().where(User.id == user_id).get().private_info
        """"""

        input_password = input_template("пароль")
        if Check_for_cmd(input_password): return cmd.get(input_password)(users)

        """"""
        get_password = PrivateHash.select().where(PrivateHash.id == password_id).get().password
        """"""

        if get_password == input_password: return Choose_state(users)
        else: 
            red_text("введен неверный пароль")
            return users.state

    async def func4(users:user)->state:#password creation
        users.password = input_template("пароль")
        if Check_for_cmd(users.password): return cmd.get(users.password)(users)
        else: return Choose_state(users)

    async def func5(users:user)->state:#password creation repeat
        repeat_password = input_template("пароль", "введите пароль повторно")
        if Check_for_cmd(repeat_password): return cmd.get(repeat_password)(users)

        if users.password == repeat_password: 

            """"""
            new_row_id = PrivateHash.insert(password = users.password).execute()
            new_user_id = User.insert(username = users.login, create_date = datetime.now().date(), create_time = datetime.now().time(), private_info = new_row_id).execute()
            """"""

            users.id = new_user_id
            return Choose_state(users)
        else: 
            red_text("введенные пароли не совпадают")
            return users.state

    async def func6(users:user)->state:#wait in menu
        return Choose_state(users)

    async def func7(users:user):#select chat
        chat_list = User_Chat.select().where(User_Chat.user_id == users.id)

        if chat_list.exists():
            print("названия доступных чатов:")
            for chat in chat_list:
                print(Chat.select().where(Chat.id == chat.chat_id).get().chat_name)

            """"""
            Name = input_template("название чата")
            """"""

            if Check_for_cmd(Name): return cmd.get(Name)(users)

            input_chat_id = Chat.select(Chat.id).where(Chat.chat_name == Name).get().id

            if input_chat_id is not None:
                users.curr_chat = input_chat_id
                return Choose_state(users)
            else:
                red_text("введено неверное название чата")
                return users.state
        else:
            red_text("у вас пока нет доступых чатов")
            return state.reverse_tree[users.state][0]

    async def func8(users:user):#create chat
        user_name = input_template("имя пользователя")
        if Check_for_cmd(user_name): return cmd.get(user_name)(users)

        """"""
        second_user_id = User.select().where(User.username == user_name)
        """"""

        if second_user_id.exists():
            green_text("пользователь найден")
            chat_name_ = input_template("название чата")
            if Check_for_cmd(chat_name_): return cmd.get(chat_name_)(users)

            second_user_id = second_user_id.get().id

            creation_date = datetime.now().date()
            creation_time = datetime.now().time() 

            """"""
            created_chat_id = Chat.insert(creator_user = users.id, create_date = creation_date,  create_time = creation_time, chat_name = chat_name_).execute()
            User_Chat.create(user_id = users.id, chat_id = created_chat_id)
            User_Chat.create(user_id = second_user_id, chat_id = created_chat_id)
            """"""

            users.curr_chat = created_chat_id
            
            return Choose_state(users)
        else:
            red_text("пользователь, которого вы хотите добавить в чат ,не найден")
            return users.state

    async def func9(users:user):#wait in chat
        return Choose_state(users)

    async def func10(users:user)->state:#message history
        #query = Chat_Message.get(Chat_Message.chat_id == users.curr_chat).message_id
        #query_2 = Message.select().where(Message.id in query).order_by(Message.create_date).get().content.id
        print("подгрузка сообщений пока не доступна")
        return Choose_state(users)
        
    async def func11(users:user)->state:#send messages
        message_ = input_template("текст сообщения")
        if Check_for_cmd(message_): 
            return cmd.get(message_)(users)

        creation_date = datetime.now().date()
        creation_time = datetime.now().time()

        message_content_id = MessageContent.insert(content = message_, content_date = creation_date, content_time = creation_time).execute()
        created_message_id = Message.insert(creator_user_id = users.id, create_date = creation_date, create_time = creation_time, content_id = message_content_id).execute()
        Chat_Message.insert(chat_id = users.curr_chat, message_id = created_message_id).execute()

        return Choose_state(users)
    
    async def func12(users:user, server:BaseServer,  conn:Connection = None)->state:#exit
        await server.send(conn, 'EXIT')
        #server.stop()


state_func = {'START':func.func0, 'SING_IN':func.func1, 'SING_UP':func.func2, 'PASS_IN':func.func3
            , 'PASS_UP':func.func4, 'PASS_REPEAT':func.func5, 'WAIT_FOR_SELECT':func.func6, 'SELECT_CHAT':func.func7
            , 'CREATE_CHAT':func.func8 , 'WAIT_IN_CHAT':func.func9, 'SEND_HISTORY':func.func10
            , 'SEND_MESSAGE':func.func11, 'EXIT':func.func12}

if __name__ == "__main__":
    
    #state_func.get(state.state_names[User1.state])(User1)
    #print(User1.state)
    #print(request.Get_id(User, User.username == 'arseny'))
    #print(User.select().where(User.username == 'arseny').get().username)
    print(User.get(User.username == 'arseny').username)
    
