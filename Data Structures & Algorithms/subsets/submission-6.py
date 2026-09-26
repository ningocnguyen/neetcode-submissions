class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []

        def dfs(i):
            if i == len(nums):
                res.append(cur[:])
                return
            
            # add nums[i]
            cur.append(nums[i])
            dfs(i+1)

            cur.pop()
            # skip nums[i]
            dfs(i+1)

        dfs(0)
        return res
