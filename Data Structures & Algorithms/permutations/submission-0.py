class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        used = [False] * n

        def dfs():
            if len(nums) == len(cur):
                res.append(cur[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                cur.append(nums[i])

                dfs()

                cur.pop()
                used[i] = False

        dfs()
        return res