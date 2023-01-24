import sys
PATH = "D:\pyton\messenger-1"
sys.path.append(PATH)

from local_objects import *
from state_class import state
from server.server.db.db_model.db_model import *
from datetime import datetime


cmd_list = ('BACK', 'EXIT')

def Check_for_cmd(string:str)->bool:
    """функция проверяет находится ли полученная строка в списке команд

    Args:
        string (str): строка для проверки

    Returns:
        bool: 
    """
    if string in cmd_list:
        return True
    else:
        return False

class cmd_func:
    """ класс функций, вызываемых в ответ на соответствующую команду
        список названий команд находится в списке cmd_list
        соответствие между функциями и командами введено в словаре cmd
    Args:
        users (user): принимает объект класса 'user'

    Returns:
        возвращает следующее состояние пользователя
        
    """
    def func0(users:user):
        if(users.state == state.state_names.index('WAIT_FOR_SELECT')):
            Connection.update(connection_end_datetime = datetime.now())
        return state.reverse_tree[users.state][0]
    def func1(users:user):
        return state.state_names.index('EXIT')

cmd = {'BACK':cmd_func.func0, 'EXIT':cmd_func.func1}

def Choose_state(users:user)->int:
    """ функция определяет следующие возможные состояния пользователя
        в случае если их более одного дает выбрать следующий шаг программы

        Args:
            users (user): принимает объект класса 'user'

        Returns:
            возвращает следующее состояние пользователя
        """
    if len(state.tree[users.state]) == 1:
        return state.tree[users.state][0]
    else:
        list = []
        for i in range(len(state.tree[users.state])):
            list.append(state.state_names[state.tree[users.state][i]])
            string = state.phrase.get(state.state_names.index(list[i]))
            print(string, list[i])
        """"""
        answer = input()
        """"""
        if Check_for_cmd(answer): return cmd.get(answer)(users)
        if answer in list: return state.state_names.index(answer)
        else:
            print("введенная команда не распознана, попробуйте еще раз")
            return users.state
