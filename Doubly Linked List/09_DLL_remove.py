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

    def pop(self):
        if self.length==0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None    
        return temp.value

    def popfirst(self):
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        self.length-=1
        return True

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        if self.length/2<index:
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length-1,index,-1):
                temp = temp.prev
        return temp

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.popfirst(index)
        if index==self.length-1:
            return self.pop(index)
        before = self.get(index-1)
        after = before.next.next
        before.next = after
        after.prev = before
        self.length-=1
        return True

myDLL = Doubly_Linked_list(3)
myDLL.append(4)
myDLL.append(5)
myDLL.append(7)
myDLL.append(9)
myDLL.remove(3)
myDLL.print()