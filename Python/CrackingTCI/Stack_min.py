class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.min = None
    

class stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        
        if not self.head:
            self.head = Node(value)
            self.head.min = value
            return

        new_node = Node(value)
        new_node.next = self.head
        new_node.min = min(value, self.head.min)
        self.head = new_node


    def print_stack(self):

        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def pop(self):
        if not self.head:
            return
        self.head = self.head.next

    def get_min(self):
        print(self.head.min)



new_stack = stack()

new_stack.push(54)
new_stack.push(5)
new_stack.push(3)
new_stack.push(100)

new_stack.print_stack()
new_stack.get_min()
new_stack.pop()
new_stack.print_stack()
new_stack.get_min()