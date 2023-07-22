class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root==None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left==None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right==None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    
    def r_contains(self,value):
        return self.__r_contains(self.root, value)
             
             
bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)


print("For 27")
print(bst.r_contains(27))

print("For 17")
print(bst.r_contains(17))