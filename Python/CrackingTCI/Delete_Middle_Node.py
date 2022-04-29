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
        return new_node

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


def delete_node(node):
    next = node.next
    node.value = next.value
    node.next = next.next




l_list = LinkedList()

l_list.push(100)
l_list.push(13)
l_list.push(2)
l_list.push(11)
l_list.push(10)
l_list.push(100)
middle = l_list.push(1234)
l_list.push(100)
l_list.print_llist()
delete_node(middle)
l_list.print_llist()
    
    