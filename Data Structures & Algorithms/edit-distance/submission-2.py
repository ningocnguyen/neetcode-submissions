class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] is the minimum operations to convert first i characters of word1 into first j characters of word 2
        
#             j=0   j=1   j=2   j=3   j=4   j=5
#             ""    "m"  "mo"  "mon" "mone" "money"
# i=0  ""  [  0,    1,    2,    3,    4,     5 ]
# i=1  "m" [  1,    0,    1,    2,    3,     4 ]
# i=2 "mo" [  2,    1,    0,    1,    2,     3 ]
# i=3"mon" [  3,    2,    1,    0,    1,     2 ]
# i=4"monk"[  4,    3,    2,    1,    1,     2 ]
# i=5"monke"[ 5,    4,    3,    2,    1,     2 ]
# i=6"monkey"[6,    5,    4,    3,    2,     1 ]
# i=7"monkeys"[7,   6,    5,    4,    3,     2 ]

        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j-1], # insert
                        dp[i-1][j], # delete
                        dp[i-1][j-1] # replace
                        ) 

        return dp[m][n]