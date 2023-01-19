cmd_list = ('BACK', 'EXIT')

def Check_for_cmd(string)->bool:
    if string in cmd_list:
        return True
    else:
        return False

class cmd_func:
    def func0():
        return 0
    def func1():
        return 0

cmd = {'BACK':cmd_func.func0, 'EXIT':cmd_func.func1}
