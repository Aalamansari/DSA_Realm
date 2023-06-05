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
    

    def is_palindrome(self):
        if self.length <= 1:
            return True
        else:
            first = self.head
            last = self.tail
            while(first != last):
                if first.value == last.value:
                    first = first.next
                    last = last.prev
                else:
                    return False
        return True



myDLL = Doubly_Linked_list(1)
myDLL.append(2)
myDLL.append(3)
myDLL.append(2)
myDLL.append(1)
val = myDLL.is_palindrome()
print(val)