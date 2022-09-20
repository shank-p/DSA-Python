"""
    To create a Binary tree using node class.
"""

class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.data)
        if self.right:
            self.right.inorderTraversal()
    
    def preorderTraversal(self):
        print(self.data)
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()



A = BinaryTreeNode(10)
A.insert(5)
A.insert(6)
A.insert(9)
A.insert(50)
A.insert(6)
A.insert(712)
A.insert(90)
A.insert(41)
A.insert(1)

A.preorderTraversal()


