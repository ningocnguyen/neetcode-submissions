# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        
        def getHeight(node):
            if not node:
                return 0 
            left = getHeight(node.left)
            right = getHeight(node.right)
            self.maxDiameter = max(self.maxDiameter, left+right)
            return 1 + max(left,right)
        
        getHeight(root)
        return self.maxDiameter
            