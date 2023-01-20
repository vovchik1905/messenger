from db_class import user

class state:
    tree = ([1, 2], [3], [4], [6], [5], [6], [7, 8], [9], [9], [10, 11] ,[9], [9])
    reverse_tree = ([], [0], [0], [1], [2], [4], [0], [6], [6], [6] ,[9], [9])
    state_names = ['START', 'LOGIN_IN', 'LOGIN_UP', 'PASS_IN', 'PASS_UP', 'PASS_REPEAT'
    , 'WAIT_FOR_SELECT', 'SELECT_CHAT', 'CREATE_CHAT' , 'WAIT_IN_CHAT', 'SEND_HISTORY', 'SEND_MESSAGE']
    phrase =    {1:"для входа введите:", 2:"для регистрации введите:", 7:"для выбора чата введите:"
                , 8:"для создания чата введите:", 10:"для подгрузки сообщений введите:", 11:"чтобы отправить сообщение введите:"}

    def next_var(value):
        return state.tree[value]
    def prev_var(value):
        return state.reverse_tree[value]

def Choose_state(users:user)->int:
    if len(state.tree[users.state]) == 1:
        return state.tree[users.state][0]
    else:
        list = []
        for i in range(len(state.tree[users.state])):
            list.append(state.state_names[state.tree[users.state][i]])
            string = state.phrase.get(i+1)
            print(string, list[i])
        answer = input()
        return state.state_names.index(answer)

if __name__ == "__main__":
    User1 = user('arseny', 0, 0, 0)
    print(Choose_state(User1))




