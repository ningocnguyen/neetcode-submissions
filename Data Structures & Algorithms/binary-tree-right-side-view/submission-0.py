# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # If this is the FIRST time we reach this depth:
            if level == len(result):
                result.append(node.val)
            
            # Go RIGHT first to ensure it's the first visitor!
            dfs(node.right, level + 1)
            # Then go left
            dfs(node.left, level + 1)
            
        dfs(root, 0)
        return result