class Node:

    def __init__(self, value) -> None:
    
        self.value = value
        self.next = None
    

class Stack:

    def __init__(self) -> None:

        self.head = None

    def push(self,value):

        new_node  = Node(value)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        self.head = new_node
        self.head.next = temp

    def pop(self):
        if self.head == None:
            return
        self.head = self.head.next

    def peek(self):
        return self.head.value

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def print_list(self):
        temp = self.head
        if self.head == None:
            return
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

        print()



    

new_stack = Stack()

new_stack.push(5)
new_stack.push(4)
new_stack.push(6)

new_stack.print_list()

new_stack.pop()

print(new_stack.peek())

new_stack.print_list()
