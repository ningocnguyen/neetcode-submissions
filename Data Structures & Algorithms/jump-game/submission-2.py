class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        max_reach = 0
        for i,jump in enumerate(nums):
            if i>max_reach:
                return False
            max_reach = max(i+jump, max_reach)
            if max_reach >= n:
                return True

        return True
            