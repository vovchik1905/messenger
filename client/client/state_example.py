class statement:
    tree = [[1, 4], [2, 3], [5], [5], [5], [0]]
    reverse_tree = [[], [0], [1], [1], [0], [2, 3, 4]]
    def __init__(self, current, last):
        self.current = current
        self.last = last
    def next(self, tree):
        return tree[self.current]
    def set(self, value):
        self.last = self.current
        self.current = value 


A = statement(0, None)

print (A.next(statement.tree))




