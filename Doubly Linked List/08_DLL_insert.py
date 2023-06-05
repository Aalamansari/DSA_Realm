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

    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
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
        return temp

    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.next = before.next
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length+=1
        return True
        

myDLL = Doubly_Linked_list(3)
myDLL.append(4)
myDLL.append(5)
myDLL.append(9)
myDLL.append(11)
myDLL.insert(2,55)
myDLL.print()