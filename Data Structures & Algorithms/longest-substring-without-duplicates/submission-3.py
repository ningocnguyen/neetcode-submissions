class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxlen=0
        charset=set()
        
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            if maxlen < (r-l+1):
                maxlen = r-l+1

            charset.add(s[r])
        

        return maxlen


