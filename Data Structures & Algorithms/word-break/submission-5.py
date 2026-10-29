class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] is the state whether the string s[:i] can be segmented (t or f)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # blank
        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[n]
