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
            return max(getHeight(node.left),getHeight(node.right))+1

        if abs(getHeight(root.left)-getHeight(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)