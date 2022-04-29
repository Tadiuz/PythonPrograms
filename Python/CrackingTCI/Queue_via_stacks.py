from inspect import stack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):

        if not self.head:
            return None
        value = self.head.value

        self.head = self.head.next
        return value
    
    def print_stack(self):
        temp = self.head
        while temp:
            print(temp.value, end="|")
            temp = temp.next

        
class MyQueue:
    def __init__(self):
        self.new_stack = None
        self.old_stack = None
    
    def rearrange(self, stack1, stack2):

        stack1 = Stack()
        print("Is here", stack2.head.value)
        while stack2.head:
            stack1.push(stack2.pop())
        return stack1

    def push(self, value):
        if not self.new_stack and not self.old_stack:
            self.new_stack = Stack()
            self.new_stack.push(value)

        if self.old_stack:
            self.new_stack = self.rearrange(self.new_stack, self.old_stack)

        self.new_stack.push(value)


    def pop(self):
        if not self.old_stack:
            self.old_stack = self.rearrange(self.old_stack, self.new_stack)

        print(self.old_stack.head.value)
        
        return self.old_stack.pop()

    def print_stacks(self):

        if self.new_stack:
            print("New stack: ")
            self.new_stack.print_stack()
            print()
        if self.old_stack:
            print("Old stack: ")
            self.old_stack.print_stack()
            print()
        

queue = MyQueue()

queue.push(56)
queue.push(54)
queue.push(33)
queue.push(23)
queue.push(6)
queue.print_stacks()
queue.pop()
queue.print_stacks()
queue.pop()
queue.print_stacks()
queue.push(6666)
queue.print_stacks()