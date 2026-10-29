class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total+target) % 2 != 0 or total < abs(target):
            return 0
        # find number of subsets whose sum equals subset_sum
        # dp[a] is number of ways to make subset_sum
        # coin change ii --> number of ways to make amount a from coins

        subset_sum = (total+target) // 2
        dp = [0] * (subset_sum+1)
        dp[0] = 1
        for n in nums:
            for a in range(subset_sum, n-1, -1):
                dp[a] += dp[a-n]

        return dp[subset_sum]

        # (1) n=2: dp[4] = 0, dp[2] = 1
        # (2) n=2: dp[4] = 1, dp[2] = 2
        # (3) n=2: dp[4] = 3, dp[2] = 3

