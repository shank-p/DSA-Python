
class TreeNode():
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            direction = input(' %d at left or right: '%data)
            if direction == 'l':
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            if direction == 'r':
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
        
T = TreeNode()
T.insert(10)
T.insert(20)
T.insert(30)
T.insert(40)

T.inorder()


def levelOrder(node: TreeNode, level) -> None:
    if node is None:
        return 
    if level == 1:
        level_nodes.append(node.data)
    elif(level > 1):
        levelOrder(node.left, level - 1)
        levelOrder(node.right, level -1)

for i in range(1, 4):
    level_nodes = []
    levelOrder(T, i)
    print(level_nodes)


def optimized_levelOrder(node: TreeNode) ->None:
    optimized = [node, None]
    while len(optimized) != 0:
        cur = optimized.pop(0)
        if cur == None:
            if len(optimized) == 0:
                return
            else:
                optimized.pop(0)
                print()
                optimized.append(None)
            continue

        print(cur.data, end=' ')
        if len(optimized) == 0:
            print()
        if cur.left is not None:
            optimized.append(cur.left)
        if cur.right is not None:
            optimized.append(cur.right)
optimized_levelOrder(T)
