from db_class import *
from command_process import *
from state_class import state

def client_handle():

    PORT = 0
    HOST = 0

    main_connection = connection(PORT, HOST)
    main_user = user('arseny', 0, 0, 0, main_connection)
    while True:
        main_user.state = state_func.get(state.state_names[main_user.state])(main_user)
        

if __name__ == "__main__":
    client_handle()