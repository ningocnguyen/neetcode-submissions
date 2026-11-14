class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # t: O(n*n!)
        # s: O(n*n!)
        
        res = []
        cur = []
        n = len(nums)
        used = [False]*n

        def backtrack():
            if len(nums) == len(cur):
                res.append(cur[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i]=True
                cur.append(nums[i])

                backtrack()

                cur.pop()
                used[i] = False

        backtrack()
        return res