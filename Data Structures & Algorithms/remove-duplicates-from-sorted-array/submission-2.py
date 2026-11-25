class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sliding window
        l=0
        # [1,1,2,2,3,4]
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                
                l+=1
                nums[l] = nums[r]
            
        return l+1