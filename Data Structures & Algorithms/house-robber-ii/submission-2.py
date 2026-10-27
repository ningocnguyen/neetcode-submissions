class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_function(nums: List[int]):
            two = 0
            one = 0
            for money in nums:
                current = max(one, two + money)
                two = one
                one = current
            return one

        return max(rob_function(nums[1:]), rob_function(nums[:-1]))

