class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp
        # similar to number of ways to make a certain target?
        # return t/f
        # subset1 = subset2 = sum(nums)/2 = target
        # dp[a] is whether sum a can be formed

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target+1)
        dp[0] = True

        for n in nums:
            if n > target:
                continue
            # backward b/c each n only used once
            for a in range(target, n-1, -1):
                dp[a] = dp[a] or dp[a-n]
            if dp[target]:
                return True

        return dp[target]


        # [1,2,3,4]

        # dp[i] is whether we cam make amount i
        # dp = [True, True, True, True, False, True]


        




        