class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking
        res, cur = [], []
        nums.sort()

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(cur[:])
            if i >= len(nums) or nums[i] > remaining:
                return
            # include num[i]
            cur.append(nums[i])
            backtrack(i, remaining - nums[i])

            # exclude nums[i]
            cur.pop()
            backtrack(i+1, remaining)

        backtrack(0, target)
        return res
