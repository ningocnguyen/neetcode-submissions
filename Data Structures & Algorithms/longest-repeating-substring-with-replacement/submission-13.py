class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        most = 0
        max_len = 0
        # track most frequent element
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            if most<count[s[r]]:
                most = count[s[r]]
            while (r-l+1) - most > k:
                count[s[l]] -= 1
                l+=1
            max_len = max(max_len, r-l+1)

        return max_len



