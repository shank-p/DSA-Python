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
    
    def postorderTraversal(self):
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()
        print(self.data)


def height(node:BinaryTreeNode)->int:
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1 

def size(node:BinaryTreeNode)->int:
    if node is None:
        return 0
    else:
        return size(node.left) + size(node.right) + 1

def max_in_tree(node):
    if node is None:
        return -999 # -infy
    else:
        return max(max_in_tree(node.left), max_in_tree(node.right), node.data)

def min_in_tree(node):
    if node is None: # +infy
        return 999
    else:
        return min(node.data, min_in_tree(node.left), min_in_tree(node.right))

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
A.insert(999)
A.insert(1000)

# height = height(A)
# print(height)
# size = size(A)
# print(size)

# max = max_in_tree(A)
# print(max)

# min = min_in_tree(A)
# print(min)
