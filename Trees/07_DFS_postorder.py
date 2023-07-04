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

    def dfs_postorder(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results
            


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_postorder())