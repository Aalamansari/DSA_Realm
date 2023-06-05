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

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        if self.length/2>index:
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length-1,index,-1):
                temp = temp.prev
        return temp.value

myDLL = Doubly_Linked_list(3)
myDLL.append(4)
myDLL.append(5)
myDLL.append(7)
myDLL.append(9)
val = myDLL.get(4)
print(val)