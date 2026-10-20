# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #     1
        #    / \
        #   2   3
        #  /   / \
        # 4   5   6
        # preorder = [1, 2, 4, 3, 5, 6]
        # inorder = [4, 2, 1, 5, 3, 6]
        in_order = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left_int, right_int):
            nonlocal pre_idx
            if left_int > right_int:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = in_order[root_val]

            root.left = helper(left_int, mid-1)
            root.right = helper(mid+1, right_int)
            
            return root
        return helper(0, len(preorder) - 1)
            # [0, 1]
            # bfs(0, 0)
            # bfs(0, -1) -> None
            # bfs(2, 1) -> None
            # bfs(2, 1) -> None

            # 1: [3, 5]
            # bfs(3, 3)
            # bfs(3, 2) -> None
            # bfs(4, 3) -> None
            # bfs(5, 5)
            # bfs(4, 5) -> None
            # bfs(6, 5) -> None


