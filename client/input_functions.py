from client.cmd import *

exeption_list = ['']

def input_template(input_atribute:str, input_message:str = None)->str:
    while True:
        if input_message is None: print("введите", input_atribute)
        else: print(input_message)
        output = input()

        if output in exeption_list or output is None:
            print ("поле", input_atribute, "нельзя оставить пустым")
            continue
        else:
            return output
