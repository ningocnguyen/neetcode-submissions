class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window
        product = 1
        res = 0
        l,r=0, 0
        for r in range(len(nums)):
            product*=nums[r]
            while l<=r and product >= k:
                product//=nums[l]
                l+=1
            res += (r-l+1)
        
        return res
