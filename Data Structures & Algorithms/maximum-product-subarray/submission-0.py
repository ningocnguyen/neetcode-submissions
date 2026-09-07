class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1

        for n in nums:
            vals = (n, n * cur_max, n * cur_min)
            cur_max = max(vals)
            cur_min = min(vals)

            res = max(res, cur_max)

        return res