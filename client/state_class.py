class state:
    tree = ([1, 2], [3], [4], [6], [5], [6], [7, 8], [9], [9], [10, 11] ,[9], [9])
    reverse_tree = ([], [0], [0], [1], [2], [4], [0], [6], [6], [6] ,[9], [9])
    state_names = ['START', 'LOGIN_IN', 'LOGIN_UP', 'PASS_UP', 'PASS_REPEAT', 'PASS_IN'
    , 'WAIT_FOR_SELECT', 'SELECT_CHAT', 'CREATE_CHAT' , 'WAIT_IN_CHAT', 'SEND_HISTORY', 'SEND_MESSAGE']

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



