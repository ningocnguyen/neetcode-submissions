class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, sol = [], []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(sol[:])
            
            if i >= len(nums) or nums[i] > remaining:
                return
            
            # include
            sol.append(nums[i])
            dfs(i, remaining - nums[i])

            # exclude
            sol.pop()
            dfs(i+1, remaining)


        dfs(0, target)
        return res