# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

      def checkNode(node,maxVal):
        if(node == None):
          return 0

        count = 0
        if(node.val >= maxVal):
          count = 1

        maxVal = max(maxVal,node.val)
        return count + checkNode(node.left,maxVal) + checkNode(node.right,maxVal)


      return checkNode(root,root.val)
