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




def detect_loop(l_list):
    temp = l_list.head
    st = set()
    while temp.next:
        if temp in st:
            return True, temp, temp.value
        st.add(temp)
        temp = temp.next
    return False







l_list_1 = LinkedList()
l_list_2 = LinkedList()

l_list_1.push(1)
l_list_1.push(2)
l_list_1.push(3)




l_list_1.head.next.next.next = l_list_1.head.next


print(l_list_1.head.next.next.next.value)


print(detect_loop(l_list_1))