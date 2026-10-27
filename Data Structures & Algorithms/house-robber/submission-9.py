class Solution:
    def rob(self, nums: List[int]) -> int:
        # define dp[i] as the maximum amount of money robbed from house 0 to i
        # dp[0] = 0
        # dp[1] = nums[0]
        # dp[2] = max(dp[1], nums[1])
        # dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])

        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        one = 0
        two = 0

        for money in nums:
            max_money = max(one, money + two)
            two = one
            one = max_money

        return one

