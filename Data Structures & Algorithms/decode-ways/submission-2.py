class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] is number of ways to decode prefix string of length i s[:i]
        # decode 1 digit: dp[i] += dp[i-1]
        # decode 2 digits
        if s[0] == '0' or not s:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            # consider 1 digit and 2 digits at every step
            # 1 digit
            if s[i-1] != '0':
                dp[i] += dp[i-1] # 10 and 12
    
            # digit
            two_digits = int(s[i-2:i])
            if 10<=two_digits<=26:
                dp[i] += dp[i-2]
        
        return dp[n]

