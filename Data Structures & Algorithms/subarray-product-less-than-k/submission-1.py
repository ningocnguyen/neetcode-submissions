class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        product = 1
        res = 0

        if k == 0:
            return 0

        for r in range(len(nums)):
            if nums[r] == k:
                return 0
            product*=nums[r]
            while l<r and product >= k:
                product //= nums[l]
                l+=1
            
            if product<=k: 
                res += (r-l+1)

        return res


        # res = 8

