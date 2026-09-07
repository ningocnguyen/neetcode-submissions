class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []

        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return

            # all subsets that include nums[i]
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()

            # all subsets that exclude nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return res


