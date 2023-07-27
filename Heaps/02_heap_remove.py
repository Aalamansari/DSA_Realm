class MaxHeap:
    def __init__(self):
        self.heap = []

    def left_child(self,index):
        return 2 *index + 1
    
    def right_child(self,index):
        return 2 * index + 2
    
    def parent(self,index):
        return (index-1)//2
    
    def swap(self,index1,index2):
        self.heap[index1], self.heap[index2] = self.heap[index2] , self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

        
    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink

myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(61)

print(myheap.heap)

myheap.insert(100)

print(myheap.heap)

myheap.insert(75)

print(myheap.heap)