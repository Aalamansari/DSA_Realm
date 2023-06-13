class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)


    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
        
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    
    def postorder_traversal(self):
        
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)


    def find(self,value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return True


tree = TreeNode(5)
tree.insert(8)
tree.insert(6)
tree.insert(9)
tree.insert(10)
tree.insert(11)
tree.insert(2)
# tree.inorder_traversal()
# tree.preorder_traversal()
# tree.postorder_traversal()
print(tree.find(1))