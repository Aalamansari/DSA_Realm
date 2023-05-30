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

    # def find_middle_node(self):
    #     if self.head == None and self.tail == None:
    #         return None
    #     slow = self.head
    #     fast = self.head
        
    #     while(fast != None and  fast.next != None):
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow.value

    def has_loop(self):
        if self.head==None and self.tail==None:
            return True
        slow = self.head
        fast = self.head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if(fast==slow):
                return True
        return False


my_linkedlist = LinkedList(3)

my_linkedlist.append(1)
my_linkedlist.append(8)
my_linkedlist.append(3)
my_linkedlist.append(6)
val = my_linkedlist.find_middle_node()
print("Middle node:",val)


my_linkedlist.print_list()