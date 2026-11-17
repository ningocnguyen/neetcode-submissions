class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2!=0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target+1)
        dp[0] = True

        # no duplicates
        # no reuse
        for n in nums:
            for a in range(target, n-1, -1):
                dp[a] = dp[a] or dp[a-n]
                if dp[target]:
                    break

        return dp[target]

        # [1,2,3,4], target = 5
        # can make dp[5]?

        # n=1: [T, T, F, F, F, F]
        # n=2: [T, T, T, T, F, F]
        # n=3: [T, T, T, T, F, T]

