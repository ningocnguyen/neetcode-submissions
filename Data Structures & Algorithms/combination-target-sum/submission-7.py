class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i >= len(nums):
                return

            # exclude
            dfs(i+1, total)

            # include
            cur.append(nums[i])
            dfs(i, total + nums[i])
            cur.pop()

        dfs(0, 0)
        return res
