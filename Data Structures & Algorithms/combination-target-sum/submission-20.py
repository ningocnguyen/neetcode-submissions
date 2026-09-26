class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        n = len(nums)
        nums.sort()

        def dfs(i, remaining):
            if remaining == 0:
                res.append(cur[:])
                return

            # out of bound
            if i >= n or remaining < nums[i]:
                return
            
            cur.append(nums[i])
            dfs(i, remaining - nums[i])
            
            cur.pop()
            dfs(i+1, remaining)
        
        dfs(0, target)
        return res