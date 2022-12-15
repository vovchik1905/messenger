class state:
    tree = ([1, 2], [3], [4], [7], [5], [6], [8], [8], [9, 10], [12], [11] ,[12], [13, 14], [12], [15], [14])
    reverse_tree = ([], [0], [0], [0], [0], [4], [5], [3], [0], [8], [8] ,[8], [8], [12], [12], [12])
    state_names = ['START', 'SING_IN', 'SING_UP', 'LOGIN_IN', 'LOGIN_UP', 'PASS_UP', 'PASS_REPEAT', 'PASS_IN'
    , 'WAIT_FOR_SELECT', 'SELECT_CHAT', 'CREATE_CHAT' ,'SELECT_USER', 'WAIT_IN_CHAT', 'SEND_HISTORY', 'SEND_MESSAGE', 'GET_MESSAGE']

    def __init__(self, current):
        self.current = current
    def next_var(self):
        return state.tree[self.current]
    def prev_var(self):
        return state.reverse_tree[self.current]
    def set(self, value):
        self.current = value 
    def state_check(self):
        print(state.state_names[self.current])



