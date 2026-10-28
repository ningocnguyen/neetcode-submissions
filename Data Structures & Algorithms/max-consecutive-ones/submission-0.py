class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        streak = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                streak = 0
            else:
                streak += 1
                max_ones = max(streak, max_ones)
        
        return max_ones
                