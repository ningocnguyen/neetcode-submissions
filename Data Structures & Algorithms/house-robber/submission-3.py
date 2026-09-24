class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        for money in nums:
            current = max(money + prev2, prev1)
            prev2 = prev1
            prev1 = current

        return current
