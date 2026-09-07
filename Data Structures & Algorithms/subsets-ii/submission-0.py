class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []

        def dfs(i, sol):
            res.append(sol[:])
            
            for index in range(i, len(nums)):
                if index > i and nums[index] == nums[index-1]:
                    continue
                sol.append(nums[index])
                dfs(index+1, sol)
                sol.pop()

        dfs(0, [])
        return res