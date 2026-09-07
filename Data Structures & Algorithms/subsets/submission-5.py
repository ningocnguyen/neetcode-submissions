class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        res, cur = [], [] 

        def dfs(i):
            if i == len(nums):
                res.append(cur[:])
                return
            
            # include nums[i]
            cur.append(nums[i])
            dfs(i+1)

            cur.pop()

            # exclude
            dfs(i+1)
            
        dfs(0)
        return res