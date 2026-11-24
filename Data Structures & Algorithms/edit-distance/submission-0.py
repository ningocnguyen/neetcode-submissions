class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] is the minimum operations to convert first i characters of word1 into first j characters of word 2
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],  # insert (left)
                        dp[i - 1][j],  # delete (top)
                        dp[i - 1][j - 1],  # replace (diagonal)
                    )

        return dp[m][n]