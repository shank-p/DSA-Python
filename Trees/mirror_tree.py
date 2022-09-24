"""
    Mirror of a Binary tree.
"""

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    
    def insert(self, data):
        if self is not None:
            pos = input('enter position to put val:')
            if pos == 'l':
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left = TreeNode(data)
            else:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right = TreeNode(data)
        else:
            self.data = data

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data)
        if self.right is not None:
            self.right.inorder()

def mirror_tree_recur(node: TreeNode) -> None:
    if node is None:
        return
    mirror_tree_recur(node.left)
    mirror_tree_recur(node.right)

    temp = node.left
    node.left = node.right
    node.right = temp        

def mirror_tree_iter(node:TreeNode) ->None:
    if node is None:
        return
    arr = [node]

    while len(arr):
        cur = arr[0]
        arr.pop(0)

        cur.left, cur.right = cur.right, cur.left
        if cur.left:
            arr.append(cur.left)
        if cur.right:
            arr.append(cur.right)



T = TreeNode(10)
T.insert(20)
T.insert(30)
T.insert(40)

T.inorder()

print()
    
mirror_tree_iter(T)
T.inorder()