class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is the fewest number of coins to make up amount i
        # dp[0] = 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        # coins = [1,2,3], a = 6
        for c in coins:
            for a in range(c, amount+1):
                dp[a] = min(1+dp[a-c], dp[a])

        return dp[amount] if dp[amount] != float('inf') else -1
        # n=1: [0, 1, 2, 3, 4, 5, 6]
        # n=2: [0, 1, 1, 2, 2, 3, 3]
        # n=3: [0, 1, 1, 1, 2, 2, 2]
