class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + jump)
            if max_reach >= target:
                return True
        
        return True