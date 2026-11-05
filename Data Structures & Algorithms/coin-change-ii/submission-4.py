class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        # dp[a] is the number of ways to make amount a
        # order of loop matters because we wouldnt want to add [2,1] when we alr have [1,2]
        # loop strictly each coin once prevent duplicates
        for c in coins:
            for a in range(c, amount+1):
                dp[a] += dp[a-c]

        return dp[amount]



        