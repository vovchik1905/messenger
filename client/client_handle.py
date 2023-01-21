from db_class import *
from command_process import *
from state_class import state

def client_handle():
    main_connection = connection(1, 1, 1)
    main_user = user('arseny', 0, 0, 0, main_connection)
    while True:
        state_func.get(state.state_names[main_user.state])(main_user)
        if main_user.state >= 9:
            break

if __name__ == "__main__":
    client_handle()