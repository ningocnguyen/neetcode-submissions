class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search: sorted, O(logn)
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            # always ensure mid is an even index
            # if nums[mid] == nums[mid+1]: target is on the right, else on the left
            if mid % 2!=0:
                mid-=1
            if nums[mid] == nums[mid+1]:
                l=mid+2
            else:
                r=mid
               
        return nums[l]
