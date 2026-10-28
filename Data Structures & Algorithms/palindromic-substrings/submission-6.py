class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n

        # 2D dp
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and (length<3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count+=1

        return count