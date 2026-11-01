class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for a in range(1, target+1):
            for c in nums:
                if a-c >= 0:
                    dp[a] += dp[a-c]

        return dp[target]

        # [1,2,3], target = 4

        # [1,1,2,4,7]

        # [1,1,1,1]
        # [1,1,2]
        # [1,2,1]
        # [1,3]
        # [2,1,1]
        # [2,2]
        # [3,1]


        