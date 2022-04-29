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

    


def sum_list(L1, L2, L3, carry):
    if not L1 and not L2:
        if carry == 1:
            L3.push(carry)
        return
    if L1:
        carry = carry + L1.value

    if L2:
        carry = carry + L2.value
    L3.push(carry%10)
    carry = carry // 10
    sum_list(L1.next if L1 else L1, L2.next if L2 else L2, L3, carry)
    return



def sum_list_follow(L1, L2, L3):
    global counter
    if not L1 and not L2:
        return 0, 1
    val = sum_list_follow(L1.next if L1 else L1, L2.next if L2 else L2, L3)
    carry = val[0]
    counter = val[1] + counter
    sum = L1.value + L2.value + carry
    L3.push(sum%10)
    carry = sum//10
    if len_max == counter:
        if carry != 0:
            L3.push(carry)
    return carry, 1



def l_len(L):

    temp = L.head
    counter = 1

    while(temp.next):
        temp = temp.next
        counter += 1
    return counter


def padding(L1, Z):

    for i in range(Z):
        L1.push(0)







l_list_1 = LinkedList()
l_list_2 = LinkedList()
l_list_3 = LinkedList()
l_list_4 = LinkedList()


l_list_1.push(6)
l_list_1.push(1)
l_list_1.push(9)

l_list_2.push(7)
l_list_2.push(2)
l_list_2.push(8)
l_list_2.push(4)
l_list_2.push(9)


sum_list(l_list_1.head, l_list_2.head, l_list_3, 0)


len_l1 = l_len(l_list_1)
len_l2 = l_len(l_list_2)

if len_l1 > len_l2:
    padding(l_list_2, len_l1 - len_l2)
    len_max = len_l1
if len_l2 > len_l1:
    padding(l_list_1, len_l2 - len_l1)
    len_max = len_l2


l_list_1.print_llist()
l_list_2.print_llist()



counter = 0
sum_list_follow(l_list_1.head, l_list_2.head, l_list_4)

l_list_4.print_llist()




