



COUNT = 10

class Node:

    def __init__(self, value) -> None:
        self.right = None
        self.left = None
        self.value = value

class BS_tree:

    def __init__(self) -> None:
        
        self.root = None

    def insert_node(self, root, value):

        if not root:
            root = Node(value)
            return root

        if value < root.value:
            root.left = self.insert_node(root.left, value)
        
        elif value > root.value:
            root.right = self.insert_node(root.right, value)

        else:
            return

        return root




    def print2DUtil(self, root, space):
 
        if (root == None):
            return
        space += COUNT

        self.print2DUtil(root.right, space)
        print()
        print(" "*(space-COUNT), end="")
        print(root.value)
        self.print2DUtil(root.left, space)



    def print2D(self):

        
        self.print2DUtil(self.root, 0)

    
    def insert(self, value):
        self.root = self.insert_node(self.root, value)



tree = BS_tree()

tree.insert(45)
tree.insert(2)
tree.insert(27)
tree.insert(50)
tree.print2D()
