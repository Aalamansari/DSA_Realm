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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def bubble_sort(self):
        if self.length<2:
            return
        sorted_until = None
        while sorted_until != self.head.next:
            current = self.head
            while current.value!=sorted_until:
                next_node = current.next
                if current.value>next_node.value:
                    temp = current.value
                    current.value = next_node.value
                    next_node.value = temp
            sorted_until = current


my_linkedlist = LinkedList(4)

my_linkedlist.append(3)
my_linkedlist.append(1)
my_linkedlist.append(2)
my_linkedlist.bubble_sort()

my_linkedlist.print_list()