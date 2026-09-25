class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] in wordSet and dp[j]:
                    dp[i] = True
                    break

        return dp[n]

