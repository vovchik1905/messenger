from input_functions import *

server_state_names = ['START', 'SING_IN', 'SING_UP', 'PASS_IN', 'PASS_UP', 'PASS_REPEAT'
    , 'WAIT_FOR_SELECT', 'SELECT_CHAT', 'CREATE_CHAT' , 'WAIT_IN_CHAT', 'SEND_HISTORY', 'SEND_MESSAGE', 'EXIT']

phrase =    {       1:"для входа введите:", 
                    2:"для регистрации введите:", 
                    7:"для выбора чата введите:", 
                    8:"для создания чата введите:", 
                    10:"для подгрузки сообщений введите:", 
                    11:"чтобы отправить сообщение введите:"}
request_phrase = {'LOGIN':'логин', 'PASSWORD':'пароль', 'PASSWORD_REPEAT':'пароль', 'CHAT_NAME':'название чата', 'USER_NAME':'имя пользователя'}

def prosess_request(received_data):
    list = received_data.split()
    if len(list) > 1:   #значит получен запрос на выбор пути по дереву состояний
        for statements in list:
            string = phrase.get(server_state_names.index(statements))
            print(string, statements)
        answer = input()   
    else:               #значит получен запрос на конкретную величину
        answer = input_template(request_phrase.get(list[0]))
    return answer
