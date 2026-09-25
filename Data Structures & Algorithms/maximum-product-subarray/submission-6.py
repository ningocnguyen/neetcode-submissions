class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val, max_val = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n*min_val, n*max_val)
            min_val = min(vals)
            max_val = max(vals)
            res = max(max_val, res)

        return res

