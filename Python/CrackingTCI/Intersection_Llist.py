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






l_list_1 = LinkedList()
l_list_2 = LinkedList()

l_list_1.push(1)
l_list_1.push(2)
l_list_1.push(3)
l_list_1.push(4)
l_list_1.push(5)

l_list_1.print_llist()


l_list_2.head = l_list_1.head.next.next.next
l_list_2.print_llist()

def len_tail(L):
    temp = L.head
    counter = 0

    while(temp):
        temp = temp.next
        counter += 1
    return counter , temp


def traverse(num, L):
    temp = L
    for i in range(num):
        temp = temp.next

    return temp


def intersection(l_list1, l_list2):
    len1, tail1 = len_tail(l_list1)
    len2, tail2 = len_tail(l_list2)

    head1 = l_list1.head
    head2 = l_list2.head

    if tail1 != tail2:
        return False

    if len1 > len2:
        head1 = traverse(len1-len2, head1)
    else:
        head2 = traverse(len2 - len1, head2)
    while True:
        if head1 == head2:
            return True, head1, head1.value
        head1 = head1.next
        head2 = head2.next




print(intersection(l_list_1, l_list_2))
