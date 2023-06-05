class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def pop(self):
        if self.length==0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head =  new_node
        self.length+=1
        return True
    
    def popfirst(self):
        if self.length==0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
        

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.value

myList = LinkedList(4)
myList.append(5)
myList.append(2)
myList.append(6)
myList.print()
val = myList.get(0)
print("Value at 1th index:",val)  