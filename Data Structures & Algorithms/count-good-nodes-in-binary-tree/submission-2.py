# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0

        def count(node, m):
            if not node:
                return 0
            if node.val >= m:
                self.count += 1
                m = node.val
            count(node.left, m)
            count(node.right, m)

        count(root, root.val)
        return self.count
        