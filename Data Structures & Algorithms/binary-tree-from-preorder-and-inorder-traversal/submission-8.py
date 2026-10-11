# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left_in: int, right_in: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left_in > right_in:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            # recurse using boundary pointers instead of slicing arrays
            root.left = helper(left_in, mid - 1)
            root.right = helper(mid + 1, right_in)

            return root

        return helper(0, len(inorder) - 1)