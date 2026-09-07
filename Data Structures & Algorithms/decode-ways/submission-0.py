class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        # run i to length n
        for i in range(2, n+1): 
            # 1 digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # 2 digit
            two_digits = int(s[i-2 : i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n]

