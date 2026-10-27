class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # iterate thru each position
        # track max_reach = max(i+nums[i], max_reach)
        # if max_reach >= len(nums) - 1 --> true
        # exit condition: i > max_reacg

        reach = 0
        n = len(nums)-1
        for i, jump in enumerate(nums):
            if i>reach:
                return False
            reach = max(reach, i+jump)
            if reach >= n:
                return True

        return True
        