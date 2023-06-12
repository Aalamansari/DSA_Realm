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

my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(4)
my_tree.insert(6)



print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)