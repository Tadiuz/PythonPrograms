class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    def print_llist(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()


l_list = LinkedList()

l_list.push(100)
l_list.push(13)
l_list.push(2)
l_list.push(11)
l_list.push(10)
l_list.append(13)
l_list.push(100)


#Recursive Way of doing
def kth_recursive(node, kth):
    if not node:
        return 0, None
    r_call = kth_recursive(node.next, kth)
    index = r_call[0]
    value = r_call[1]
    counter = index + 1
    if counter == kth:
        value = node.value

    return counter, value

print(kth_recursive(l_list.head, 3))


#Iterative Way


def kth_iterative(node, kth):
    p1 = node
    p2 = node
    for i in range(kth - 1):
        if not p2.next:
            return None
        p2 = p2.next
    while p2.next:
        p1 = p1.next
        p2 = p2.next
    return p1.value

print(kth_iterative(l_list.head, 30))
l_list.print_llist()



    
    