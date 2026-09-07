# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(node, level):
            if not node:
                return None
            if len(res) == level:
                # not knowing how many levels yet 
                res.append([])
            res[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        
        bfs(root, 0)
        return res