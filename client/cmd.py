from db_class import *
from state_class import state

cmd_list = ('BACK', 'EXIT')

def Check_for_cmd(string)->bool:
    if string in cmd_list:
        return True
    else:
        return False

class cmd_func:
    def func0(users:user):
        return state.reverse_tree[users.state][0]
    def func1(users:user):
        return 12

cmd = {'BACK':cmd_func.func0, 'EXIT':cmd_func.func1}

def Choose_state(users:user)->int:
    if len(state.tree[users.state]) == 1:
        return state.tree[users.state][0]
    else:
        list = []
        for i in range(len(state.tree[users.state])):
            list.append(state.state_names[state.tree[users.state][i]])
            string = state.phrase.get(state.state_names.index(list[i]))
            print(string, list[i])
        answer = input()
        if Check_for_cmd(answer): return cmd.get(answer)(users)
        if answer in list: return state.state_names.index(answer)
        else:
            print("введенная команда не распознана, попробуйте еще раз")
            return users.state
