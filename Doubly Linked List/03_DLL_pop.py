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
        
    # def pop(self):
    #     if self.length == 0:
    #         return None
        
    #     temp = self.tail
        
    #     if self.length == 1:
    #         self.head = None
    #         self.tail = None
    #     else:    
    #         self.tail = self.tail.prev
    #         temp.prev = None
    #         self.tail.next = None
    
    #     self.length -= 1
    #     return temp.value

myDLL = Doubly_Linked_list(3)
myDLL.append(4)
myDLL.append(5)
print(myDLL.pop())