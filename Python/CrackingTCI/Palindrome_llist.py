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



l_list_1 = LinkedList()


l_list_1.push('a')
l_list_1.push('b')
l_list_1.push('c')
l_list_1.push('b')
l_list_1.push('a')

l_list_1.print_llist()


counter = 0
len = l_len(l_list_1)
middle = len/2 if len%2 == 0 else len/2 + 1

head = l_list_1.head

def is_palindrome(l_list):
    global counter
    global head
    if not l_list:
        return True
    if(is_palindrome(l_list.next if l_list else l_list )):
        if counter < middle:
            if head.value != l_list.value:
                return False
            head = head.next
            counter +=1
        return True
    return False


print(is_palindrome(l_list_1.head))





