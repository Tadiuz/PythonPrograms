
from datetime import datetime



class Node:
    def __init__(self, value, date):
        self.next = None
        self.value = value
        self.date = date

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        time = datetime.now()
        new_node = Node(value, time)
        new_node.next = self.head

        self.head = new_node
    def pop(self):

        if not self.head:
            return None

        value = self.head.value
        self.head = self.head.next
        return value

    def print(self):
        l = []
        temp = self.head
        while temp:
            l.append(temp.value)
            temp = temp.next
        print(l)


class animal_shelter:
    def __init__(self):
        self.dogs = Stack()
        self.cats = Stack()

    def enqeue_dog(self, name): self.dogs.push(name)
    def enqeue_cats(self, name): self.cats.push(name)

    def deque_any(self):
        dog = self.dogs.head.date
        cat = self.cats.head.date

        if dog < cat:
            self.dogs.pop()
            return
        self.cats.pop()

    def print(self):
        self.dogs.print()
        self.cats.print()

animal = animal_shelter()
animal.enqeue_dog("Tomy")
animal.enqeue_dog("Black")
animal.enqeue_cats("Lia")

animal.print()