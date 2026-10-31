class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[c] is the number of ways to reach cell (r,c)
        dp = [1] * (n)
        
        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c]+dp[c-1]

        return dp[n-1]
