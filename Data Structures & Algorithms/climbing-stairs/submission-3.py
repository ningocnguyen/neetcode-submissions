class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] as the number of ways to reach to stair i
        # dp[i] = dp[i-1] + dp[i-2]

        # # 1D dp table
        # dp = [0] * (n+1)
        # if n<=2: 
        #     return n
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-2] + dp[i-1]

        # return dp[i]

        # optimized way
        if n<=2: 
            return n
        two = 1
        one = 2

        for i in range(3, n+1):
            current = one + two
            two = one
            one = current

        return current

