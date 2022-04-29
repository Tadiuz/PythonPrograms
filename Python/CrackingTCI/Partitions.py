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


# def two_arrays(l_list, target):
#     lower = []
#     greater = []
#     temp = l_list.head
#     while temp:
#         if temp.value < target:
#             lower.append(temp.value)
#         else:
#             greater.append(temp.value)
#         temp  = temp.next
#     lower.extend(greater)
#     temp = l_list.head
#     for i in lower:
#         temp.value = i
#         temp = temp.next


# print("Two Arrays  ")
# l_list = LinkedList()
# l_list.push(1)
# l_list.push(2)
# l_list.push(3)
# l_list.push(4)
# l_list.push(100)
# l_list.push(1000)
# l_list.push(34)
# l_list.push(3)
# l_list.push(234)
# l_list.push(89)
# l_list.print_llist()
# two_arrays(l_list, 4)
# l_list.print_llist()



# def push_pop(l_list, target):
#     l_aux = LinkedList()

#     temp = l_list.head

#     while temp:
#         if temp.value < target:
#             l_aux.push(temp.value)
#         else:
#             l_aux.append(temp.value)

#         temp = temp.next
    
#     return l_aux


# print("Push Pop")
# l_list = LinkedList()
# l_list.push(1)
# l_list.push(2)
# l_list.push(3)
# l_list.push(4)
# l_list.push(100)
# l_list.push(1000)
# l_list.push(34)
# l_list.push(3)
# l_list.push(234)
# l_list.push(89)
# l_list.print_llist()
# l_list = push_pop(l_list, 4)
# l_list.print_llist()



def two_llist(l_list, target):

    l_left = LinkedList()
    l_right = LinkedList()

    temp = l_list.head
    while temp:
        if temp.value < target:
            l_left.append(temp.value)
        else:
            l_right.append(temp.value)
        temp = temp.next

    temp = l_left.head
    while temp.next:
        temp = temp.next

    temp.next = l_right.head

    return l_left

print("Push Pop")
l_list = LinkedList()
l_list.push(1)
l_list.push(2)
l_list.push(3)
l_list.push(4)
l_list.push(100)
l_list.push(1000)
l_list.push(34)
l_list.push(3)
l_list.push(234)
l_list.push(89)
l_list.print_llist()
l_list = two_llist(l_list, 4)
l_list.print_llist()