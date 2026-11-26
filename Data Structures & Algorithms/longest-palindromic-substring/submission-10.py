class Solution:
    def longestPalindrome(self, s: str) -> str:
        # i/j 0 1 2 3 4
        #     a b a b d
        # 0 a T   T
        # 1 b   T   T
        # 2 a     T
        # 3 b       T
        # 4 d         T


        # dp[i][j] true if s[i] == s[j] and (dp[i+1][j-1] also true or j-i<=3)

        n=len(s)
        dp = [[False]*n for i in range(n)]
        max_len = 1
        start = 0

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and (length<=3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if length > max_len:
                        max_len = length
                        start = i

        return s[start:start+max_len]



        


