class Solution:
    def rob(self, nums: List[int]) -> int:
        # define dp[i] as the maximum amount of money robbed till house i
        # dp[0] = 0
        # dp[1] = nums[0]
        # dp[2] = max(dp[1], nums[1])
        # dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])

        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[n-1]

