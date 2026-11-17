class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] is number of ways to make up amount a
        # += 
        # outer loop: coins
        # inner: amount
        dp = [0] * (amount+1)
        dp[0] = 1
        for c in coins:
            for a in range(c, amount+1):
                dp[a] += dp[a-c]

        return dp[amount]

        # [1,2,5], amount = 5
        # c=1: [1,1,1,1,1,1]
        # c=2: [1,1,2,2,3,3] 11111, 1112, 122
        # c=5: [1,1,2,2,3,4] 5
