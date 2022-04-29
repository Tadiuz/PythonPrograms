class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

def height(root):
    if root == None:
        return -1
    return max(height(root.right), height(root.left)) +1

def balance_factor(root):
    return height(root.left) - height(root.right)

def left_rotation(root):
    aux1 = root.right
    aux2 = aux1.left

    aux1.left = root
    root.right = aux2
    return aux1

def right_rotation(root):
    aux1 = root.left
    aux2 = aux1.right

    aux1.right = root
    root.left = aux2
    return aux1
    
def insert(root, value):
    if root == None:
        root = Node(value)
        return root
    elif value > root.value:
        root.right = insert(root.right, value)
    elif value < root.value:
        root.left = insert(root.left, value)

    bf = balance_factor(root)

    if bf < -1 and root.right.value < value:
        root = left_rotation(root)

    elif bf > 1 and root.left.value > value:
        root = right_rotation(root)

    elif bf > 1 and root.left.value < value:
        root.left = left_rotation(root.left)
        root = right_rotation(root)

    elif bf < -1 and root.right.value > value:
        root.right = right_rotation(root.right)
        root = left_rotation(root)
    return root


def minValue(root):
    temp = root
    while (temp.left !=None):
        temp = temp.left
    return temp


def deleteNode(root, value):
    if root == None:
        return root
    if value > root.value:
        root.right = deleteNode(root.right, value)
    elif value < root.value:
        root.left = deleteNode(root.left, value)
    else: #Case the value is equal
        if root.right == None:
            return root.left
        elif root.left == None:
            return root.right
        else: #The node has two nodes, so lets find  the minimum value from the right sub-tree
            temp = minValue(root.right)
            root.value = temp.value
            root.right = deleteNode(root.right, temp.value)

    bf = balance_factor(root)

    if bf >1 and balance_factor(root.left) >= 0:
        root = right_rotation(root)
    
    elif bf > 1 and balance_factor(root.left) ==-1:
        root.left = left_rotation(root.left)
        root = right_rotation(root)
    
    elif  bf < -1 and balance_factor(root.right) <=0:
        root = left_rotation(root)

    elif bf < -1 and balance_factor(root.right) ==1:
        root.right = right_rotation(root.right)
        root = left_rotation(root)
    
    return root


def print2Droot(root, space):
    if root == None:
        return
    space = space + 10
    print2Droot(root.right, space)
    print(" "*space,root.value)
    print()
    print2Droot(root.left, space)


# root = Node(9)
# root = insert(root, 7)
# root = insert(root, 10)
# root = insert(root, 6)
# root = insert(root, 8)
# root = insert(root, 11)
# root = insert(root, 4)
# root = insert(root, 5)
# print2Droot(root, 0)
# print(height(root))
# print(balance_factor(root))

# root = Node(15)
# root = insert(root, 10)
# root = insert(root, 20)
# root = insert(root, 5)
# root = insert(root, 11)
# root = insert(root, 19)
# root = insert(root, 30)
# root = insert(root, 29)
# root = insert(root, 19)
# root = insert(root, 17)
# root = insert(root, 4)
# root = insert(root, 18)
# root = insert(root, 16)
# root = deleteNode(root, 15)

# print2Droot(root, 0)


root = Node(15)
root = insert(root, 20)
root = insert(root, 10)
root = insert(root, 11)
root = insert(root, 9)
root = insert(root, 21)
root = insert(root, 10.5)

print2Droot(root, 0)

root = deleteNode(root, 20)

print2Droot(root, 0)