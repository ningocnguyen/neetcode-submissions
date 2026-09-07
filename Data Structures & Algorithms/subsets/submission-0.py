class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            # base case
            if i == n:
                res.append(list(sol))
                return 

            # dont pick nums[i]
            backtrack(i+1)
            
            # pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)

            sol.pop()

        backtrack(0)
        return res