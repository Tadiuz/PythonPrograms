class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size +=1

    def pop(self):
        if not self.head:
            return

        value = self.head.value
        self.head = self.head.next
        self.size -=1
        return value

    def get_size(self):
        return self.size

    def print_stacks(self):
        temp = self.head
        while temp:
            print(temp.value, end="|")
            temp = temp.next

class set_of_stacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        return self.stacks[-1]

    def create_stack(self, value):
        new_stack = stack()
        new_stack.push(value)
        self.stacks.append(new_stack)


    def push(self, value):
        if not self.stacks:
            self.create_stack(value)
        last = self.get_last_stack()

        if last.get_size() == self.capacity:
            self.create_stack(value)
            return 
        last.push(value)

    def pop(self):
        if not self.stacks:
            return
        last = self.get_last_stack()

        if last.get_size() == 0:
            del self.stacks[-1]
            last = self.get_last_stack()
        
        if self.stacks:
            return last.pop()
            
        
    def print_stacks(self):
        
        for i in self.stacks:
            i.print_stacks()
            print(end = "**")
        print()
        
        
stacks = set_of_stacks(5)

stacks.push(89)
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
stacks.push(6)
stacks.push(7)
stacks.push(8)
stacks.push(9)
stacks.print_stacks()

