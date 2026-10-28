class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is the fewest number of coins to make up amount i
        # dp[i] = min(dp[])
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        # coins = [1,2,3]
        # amount = 6

        for a in range(amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(1 + dp[a-c], dp[a])

        return dp[amount] if dp[amount] != float('inf') else -1