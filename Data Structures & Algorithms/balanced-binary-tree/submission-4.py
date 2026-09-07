# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def getHeight(node):
            if not node:
                return 0 
            left=getHeight(node.left)
            right=getHeight(node.right)
            return 1+max(left,right)
        
        if abs(getHeight(root.left)-getHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)