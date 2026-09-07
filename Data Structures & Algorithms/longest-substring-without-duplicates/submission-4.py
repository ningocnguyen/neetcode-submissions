class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        max_len = 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            if max_len < (r-l+1):
                max_len = r-l+1
            charset.add(s[r])

        return max_len
