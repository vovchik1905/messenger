def input_template(input_atribute:str, input_message:str = None)->str:
    while True:
        if not input_message: print("введите {input_atribute} \n")
        else: print(input_message + "\n")
        output = input()
        if output == None:
            print ("поле {input_atribute} нельзя оставить пустым\n")
            continue
        else:
            return output

class func:
    def func0():
        return input_template("логин")
    def func1():
        return input_template("пароль")
    def func2():
        return input_template("пароль", "введите пароль повторно")
    def func3():
        return 0
    def func4():
        return 0
    def func5():
        return input_template("текст сообщения")

request = {'LOGIN':func.func0, 'PASSWORD':func.func1, 'PASSWORD_REPEAT':func.func2,
'CHAT_SELECT':func.func3,'CHAT_CREATE':func.func4,'TYPE_MESSAGE':func.func5}