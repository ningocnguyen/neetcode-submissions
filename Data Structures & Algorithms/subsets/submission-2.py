class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def dfs(i):
            if i == n:
                res.append(sol[:])
                return

            # exclude nums[i]
            dfs(i+1)

            # include nums[i]
            sol.append(nums[i])
            dfs(i+1)

            sol.pop()

        dfs(0)
        return res
