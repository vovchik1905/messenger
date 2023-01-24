from local_objects import *
from main_functions import *
from state_class import state

def client_handle():
    """ основная функция
        создает бесконечный цикл в котором осуществляет обработку и изменение состояния пользователя
        цикл прерывается если получена команда 'EXIT'
    """

    PORT = 5001
    HOST = 1

    main_connection = connection(PORT, HOST)
    main_user = user('arseny', 0, 0, 0, main_connection)
    
    while True:
        main_user.state = state_func.get(state.state_names[main_user.state])(main_user)
        

if __name__ == "__main__":
    client_handle()