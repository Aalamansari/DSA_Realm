class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length=1

    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        if self.length==0:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.last
            temp.next = new_node
            self.last = new_node
        self.length+=1
        return True
    
my_queue = Queue(4)
my_queue.enqueue(5)
my_queue.enqueue(7)
my_queue.enqueue(6)
my_queue.print()