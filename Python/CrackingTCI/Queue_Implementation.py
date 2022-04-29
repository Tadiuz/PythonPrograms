class Node:

    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.head = self.tail  = None
    
    def enqueue(self, value):

        t = Node(value)

        if self.tail == None:
            self.tail = t
            self.head = self.tail
            return
        self.tail.next = t
        self.tail = self.tail.next


    def dequeue(self):

        if self.head == None: 
            self.head = self.tail = None
            return None

        value = self.head.value
        self.head = self.head.next



        return value

    def front(self): return self.head.value
    def rear(self): return self.tail.value
        


    def print_queue(self):
        temp = self.head

        while temp:
            print(temp.value, end = " ")
            temp = temp.next
        print()


queue = Queue()

queue.enqueue(5)
queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(8)
# queue.print_queue()

# print(queue.front())
# print(queue.rear())


# print(queue.dequeue())
# queue.print_queue()

# print(queue.dequeue())
# queue.print_queue()

# print(queue.dequeue())
# queue.print_queue()

# print(queue.dequeue())
# queue.print_queue()

# print(queue.dequeue())
# queue.print_queue()

# print("New One")
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(8)
# queue.print_queue()

# print(queue.dequeue())
# queue.print_queue()