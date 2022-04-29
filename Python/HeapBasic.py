class MinHeap:
    def __init__(self):
        self.array = []
        self.len_heap = 0

    def parent(self,i):
        return int((i-1)/2)

    def leftvalue(self,i):
        return int((2*i)+1)

    def rightvalue(self,i):
        return int((2*i)+2)

    def swap(self, i, parent):
        self.array[i], self.array[parent] =  self.array[parent], self.array[i]
    
    def insert_value(self, value):
        self.array.append(value)
        self.len_heap += 1

        i = self.len_heap -1

        while (i!=0 and self.array[i] < self.array[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, i):
        smallest = i

        l = self.leftvalue(i)
        r = self.rightvalue(i)

        if l < self.len_heap and self.array[l] < self.array[i]: smallest = l
        if r < self.len_heap and self.array[r] < self.array[smallest]: smallest = r

        if smallest !=i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def extractMin(self):
        if self.len_heap <=0:
            return
        if self.len_heap == 1:
            self.len_heap -=1
            a = self.array.pop()
            return a

        minimum = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.len_heap -=1
        self.heapify(0)
        return minimum


    def print_heap(self):
        print(self.array)


    def delete(self, value):
        index = self.array.index(value)
        self.array[index] = float('-inf')
        while (index !=0 and self.array[self.parent(index)] > self.array[index]):
            self.swap(index, self.parent(index))
            index = self.parent(index)
        self.extractMin()

    def biggerthank(self, k):
        if any(map(lambda x: x < k, self.array)) or len(self.array) == 0:
            return True
        return False

# heap = MinHeap()

# heap.insert_value(5)
# heap.insert_value(7)
# heap.insert_value(10)
# heap.insert_value(2)
# heap.insert_value(9)
# heap.insert_value(1)
# heap.print_heap()
# heap.extractMin()
# heap.print_heap()
# heap.delete(7)
# heap.print_heap()
# heap.insert_value(1)
# heap.print_heap()
# heap.insert_value(0)
# heap.print_heap()
# heap.delete(1)
# heap.print_heap()
# heap.insert_value(3)
# heap.print_heap()
# heap.insert_value(0.5)
# heap.print_heap()
# print(heap.biggerthank(8))
    
# heap = MinHeap()
# heap.insert_value(1)
# heap.print_heap()
# heap.extractMin()
# heap.print_heap()


heap = MinHeap()

heap.insert_value(8)
heap.insert_value(77)
heap.insert_value(10)
heap.insert_value(72)
heap.insert_value(1)
heap.insert_value(10)
heap.insert_value(100)
heap.insert_value(1000)
heap.print_heap()
print(heap.biggerthank(8))
print()



heap = MinHeap()

heap.insert_value(72)
heap.insert_value(10)
heap.insert_value(8)
heap.insert_value(77)
heap.insert_value(1000)
heap.insert_value(100)
heap.insert_value(10)
heap.insert_value(1)
heap.print_heap()
print(heap.biggerthank(8))