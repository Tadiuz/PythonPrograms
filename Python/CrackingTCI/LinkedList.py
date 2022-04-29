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

    
    def remove_duplicates(self):
        unique_values = set()
        temp = self.head
        while temp:
            if temp.value in unique_values:
                prev.next = temp.next
            else:
                unique_values.add(temp.value)
                prev = temp
                
            temp = temp.next



l_list = LinkedList()



l_list.push(100)
l_list.push(13)

temp = l_list.head


print(temp.next.next or "Hola")









    
    