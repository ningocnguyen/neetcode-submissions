class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach > target:
                return True
        
        return True
            