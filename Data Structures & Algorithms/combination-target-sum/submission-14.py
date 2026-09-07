class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def dfs(i, total):
            if total == target:
                res.append(sol[:])
                return
            
            if i >= len(nums) or total > target:
                return
            
            # include
            sol.append(nums[i])
            dfs(i, total + nums[i])

            # exclude
            sol.pop()
            dfs(i+1, total)


        dfs(0, 0)
        return res