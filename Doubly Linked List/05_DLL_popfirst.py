class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None

class Doubly_Linked_list:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp!=None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length==None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev =self.tail
            self.tail = new_node
        self.length+=1
        return True
    
    def popfirst(self):
        if self.length==0:
            return None
        temp = self.head.next
        self.head.next = None
        self.head.prev = None
        self.head = temp
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return True

myDLL = Doubly_Linked_list(3)
myDLL.append(4)
myDLL.append(5)
myDLL.popfirst()
myDLL.print()