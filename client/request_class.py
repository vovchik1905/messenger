from client.cmd import *

def input_template(input_atribute:str, input_message:str = None)->str:
    while True:
        if input_message is None: print("введите", input_atribute)
        else: print(input_message)
        output = input()

        if output is None:
            print ("поле", input_atribute, "нельзя оставить пустым")
            continue
        else:
            return output

"""class func:
    def func0():
        return input_template("логин")
    def func1():
        return input_template("пароль")
    def func2():
        return input_template("пароль", "введите пароль повторно")
    def func3():
        return input_template("название чата")
    def func4():
        return input_template("имя пользователя")
    def func5():
        return input_template("текст сообщения")

request = {'LOGIN':func.func0, 'PASSWORD':func.func1, 'PASSWORD_REPEAT':func.func2,
'CHAT_SELECT':func.func3,'CHAT_CREATE':func.func4,'TYPE_MESSAGE':func.func5}"""
    
