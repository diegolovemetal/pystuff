class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_tree(root, space=0, t=0):
        COUNT = 3
        if root is None:
            return

        space += COUNT

        print_tree(root.right, space, 1)

        for x in range(count, space):
            print(" ", end = " ")
        #right
        if t == 1:
            print("/ ", root.data)
        if t == 2:
            print("\ ", root.data)
        #root
        else:
            print(root.data)

        print_tree(root.left, space, 2)


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
print_tree(root) 

