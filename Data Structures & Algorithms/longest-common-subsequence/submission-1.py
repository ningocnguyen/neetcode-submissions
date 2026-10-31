class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d dp
        # dp[i][j] is LCS of text1 of length i and text2 of length j

        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # i/j  0 1 2 3 4 5 
        # 0    0 0 0 0 0 0
        # 1    0 1 1 1 1 1
        # 2    0 1 1 2 2 2
        # 3    0 1 1 2 2 3

        for i in range(1, m+1):
            for j in range(1, n+1):
                # match
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                # not match
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]