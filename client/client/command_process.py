from state_class import state

def func0(x):
    print('0' + str(x))
def func1(x):
    print('1' + str(x))
def func2(x):
    print('2' + str(x))
def func3(x):
    print('3' + str(x))
def func4(x):
    print('4' + str(x))
def func5(x):
    print('5' + str(x))
def func6(x):
    print('6' + str(x))
def func7(x):
    print('7' + str(x))
def func8(x):
    print('8' + str(x))
def func9(x):
    print('9' + str(x))
def func10(x):
    print('10' + str(x))
def func11(x):
    print('11' + str(x))
def func12(x):
    print('12' + str(x))
def func13(x):
    print('13' + str(x))
def func14(x):
    print('14' + str(x))
def func15(x):
    print('15' + str(x))

state_func = {'START':func0, 'SING_IN':func1, 'SING_UP':func2, 'LOGIN_IN':func3, 'LOGIN_UP':func4
            , 'PASS_UP':func5, 'PASS_REPEAT':func6, 'PASS_IN':func7, 'WAIT_FOR_SELECT':func8, 'SELECT_CHAT':func9
            , 'CREATE_CHAT':func10 ,'SELECT_USER':func11, 'WAIT_IN_CHAT':func12, 'SEND_HISTORY':func13
            , 'SEND_MESSAGE':func14, 'GET_MESSAGE':func15}

state_func.get(state.state_names[5])(10)
