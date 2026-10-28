class Solution:
    def longestPalindrome(self, s: str) -> str:

    #     0 1 2 3 4
    #     a b a b d
    # 0 a T   T
    # 1 b   T   T
    # 2 a     T
    # 3 b       T
    # 4 d         T       
        
        # start end pointer of DP
        # dp[i][j] is True if (dp[i+1][j-1] also True if j-i>=3) and (s[i] == s[j])

        n = len(s)
        max_len = 1
        start = 0

        # 2D dp
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and (length<=3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if max_len < length:
                        max_len = length
                        start=i

        return s[start:start+max_len]



        
