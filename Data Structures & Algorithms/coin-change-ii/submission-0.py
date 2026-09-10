class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] is the amount of ways to make amount a
        dp = [0]*(amount+1)
        dp[0] = 1
        
        # count combination, not permutation
        for c in coins: # process in strict order
            for a in range(c, amount+1):
                dp[a] += dp[a-c]
        
        return dp[amount]