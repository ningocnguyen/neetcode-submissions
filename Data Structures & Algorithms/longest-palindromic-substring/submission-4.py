class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming
        # nxn table dp
        n = len(s)
        dp = [[False]*n for i in range(n)]
        max_len = 1
        start = 0

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n+1): # up to length
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j]:
                    if length<=3 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if max_len < length:
                            max_len = length
                            start = i

        return s[start:start+max_len]
