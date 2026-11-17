class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # permutation
        # [1,2] and [2,1] are possible combinations
        # coin change II: [1,2] and [2,1] are the same --> coins as outer loop
        # dp[a] is number of possible combinations that add to target
        dp = [0] * (target+1)
        dp[0] = 1

        # [3,1,2], target = 4

        # t=1: [1,1,0,0,0] [1]
        # t=2: [1,1,2,0,0] \\ [1,1], [2]
        # t=3: [1,1,2,4,0] \\ [3], [1,1,1], [2,1], [1,2]
        # t=4: [1,1,2,4,7] \\ [1,3], [3,1], [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
        for t in range(target+1):
            for n in nums:
                if n>t:
                    continue
                dp[t] += dp[t-n]

        return dp[target]