class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sol,res=[],[]

        def backtrack(i):
            if i == n:
                res.append(list(sol))
                return
            
            # exclude
            backtrack(i+1)

            # include
            sol.append(nums[i])
            backtrack(i+1)

            sol.pop()

        backtrack(0)
        return res