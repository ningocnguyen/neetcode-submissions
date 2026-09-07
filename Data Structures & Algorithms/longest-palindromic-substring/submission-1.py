class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1 # ending index

                if s[i] == s[j]:
                    if length <= 3 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if length > max_len:
                            max_len = length
                            start = i

        return s[start:start+max_len] 