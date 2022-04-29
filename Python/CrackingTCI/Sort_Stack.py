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
    
    def print(self):
        lista = []

        temp = self.head
        while temp:
            lista.append(temp.value)
            temp = temp.next
        print(lista)


class Sstack:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def sort(self):

        while self.stack_1.head:
            value = self.stack_1.pop()
            while True:
                print("Here", value)
                if not self.stack_2.head or self.stack_2.head.value >= value:
                    self.stack_2.push(value)
                    break
                else:
                    self.stack_1.push(self.stack_2.pop())

                    
    def push(self, value):
        self.stack_1.push(value)
        self.sort()

    def pop(self):
        return self.stack_2.pop()

    def print(self):
        self.stack_2.print()


stack = Sstack()

stack.push(34)
stack.push(345)
stack.push(234)
stack.push(43)
stack.push(2)
stack.push(223)
stack.push(543)
stack.print()
print(stack.pop())


