class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid=(l+r)//2 # floor division

            if nums[mid] == target:
                return mid

            # search in first half
            if nums[mid] >= nums[l]: # floor division # [3,1]
                if nums[mid]<target or target < nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            # search in first half
            else:
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1

        return -1