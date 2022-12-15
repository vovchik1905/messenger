class statement:
    tree = ([1, 4], [2, 3], [5], [5], [5], [0])
    reverse_tree = ([], [0], [1], [1], [0], [2, 3, 4])
    def __init__(self, current):
        self.current = current
    def next_var(self):
        return statement.tree[self.current]
    def prev_var(self):
        return statement.reverse_tree[self.current]
    def set(self, value):
        self.current = value 
   
    


A = statement(0)

print (A.next_var())
txt = input("введите следующий элемент")
A.set(int(txt))
print(A.current)
print(A.next_var())




