from client.local_objects import user

class state:
    tree = ([1, 2], [3], [4], [6], [5], [6], [7, 8], [9], [9], [10, 11] ,[9], [9])
    reverse_tree = ([0], [0], [0], [1], [2], [4], [0], [6], [6], [6] ,[9], [9])
    state_names = ['START', 'LOGIN_IN', 'LOGIN_UP', 'PASS_IN', 'PASS_UP', 'PASS_REPEAT'
    , 'WAIT_FOR_SELECT', 'SELECT_CHAT', 'CREATE_CHAT' , 'WAIT_IN_CHAT', 'SEND_HISTORY', 'SEND_MESSAGE', 'EXIT']
    phrase =    {1:"для входа введите:", 2:"для регистрации введите:", 7:"для выбора чата введите:"
                , 8:"для создания чата введите:", 10:"для подгрузки сообщений введите:", 11:"чтобы отправить сообщение введите:"}

    def next_var(value):
        return state.tree[value]
    def prev_var(value):
        return state.reverse_tree[value]




