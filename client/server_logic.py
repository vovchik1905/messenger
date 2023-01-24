from local_objects import *
from main_functions import *
from state_class import state

def client_handle(main_user:user):

    
    while True:
        main_user.state = state_func.get(state.state_names[main_user.state])(main_user)
        

if __name__ == "__main__":
    client_handle()