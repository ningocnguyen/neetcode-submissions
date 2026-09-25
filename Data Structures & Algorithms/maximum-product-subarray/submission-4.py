class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val, max_val = 0, 0
        res = 0
        if len(nums) == 1:
            return nums[0]

        for n in nums:
            vals = (n, n*min_val, n*max_val)
            min_val = min(vals)
            max_val = max(vals)
            res = max(max_val, res)

        return res

