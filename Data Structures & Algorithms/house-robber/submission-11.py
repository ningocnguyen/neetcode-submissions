class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] as maximum money robbed from house 0 to house i to not get caught
        # dp = [0] * (n) where n = len(nums)
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        n = len(nums)
        dp = [0] * (n)
        if not nums:
            return 0
        if len(nums) == 2:
            return max(nums)

        one = 0
        two = 0

        for n in nums:
            max_money = max(one, two+n)
            two = one
            one = max_money

        return max_money