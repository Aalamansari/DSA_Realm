class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None

class Doubly_Linked_list:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def print(self):
        temp = self.head
        while temp!=None:
            print(temp.value)
            temp = temp.next

    