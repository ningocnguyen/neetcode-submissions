class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return

            if total > target or i >= len(nums):
                return

            # include
            cur.append(nums[i])
            dfs(i, total + nums[i])

            # exclude
            cur.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return res