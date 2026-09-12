class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # single use of each num
        # subset_target = (total_sum + target) // 2

        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0

        subset_target = (total_sum + target) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1

        for num in nums:
            for w in range(subset_target, num-1, -1):
                dp[w] += dp[w-num]
        
        return dp[subset_target]

