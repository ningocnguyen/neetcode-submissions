class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p, min_p = 1, 1
        max_product = nums[0]
        for n in nums:
            save = (n, max_p*n, min_p*n)
            min_p = min(save)
            max_p = max(save)
            if max_product < max_p:
                max_product = max_p
        return max_product

        
        # nums = [2,4,-3,-5]
        # n=2: (2, 1, 1) -> max = 2, min = 1
        # n=4: (8, 2, 1) -> max = 8, min = 1
        # n=-3: (-24, 8, 1) -> max = 8, min = -24
        # n=-5L (120, 8, -24) -> max = 120, min = -24



