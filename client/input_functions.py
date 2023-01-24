from client.cmd import *

exeption_list = ['']
"""список строк/символов - исключений для ввода
"""

def input_template(input_atribute:str, input_message:str = None)->str:
    """шаблон для ввода ответа пользователем


    Args:
        input_atribute (str): переменная, которую должен ввести пользователей
        input_message (str, optional): сообщение которое необходимо показать пользователю при вводе. Defaults to None.

    Returns:
        str: ответ пользователя 
    """
    while True:
        if input_message is None: print("введите", input_atribute)
        else: print(input_message)
        output = input()

        if output in exeption_list or output is None:
            print ("поле", input_atribute, "нельзя оставить пустым")
            continue
        else:
            return output
