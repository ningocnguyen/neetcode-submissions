class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        charset=set()
        max_len=0

        while r<len(s):
            while s[r] in charset:
                    charset.remove(s[l])
                    l+=1
            charset.add(s[r])
            if max_len<(r-l+1):
                max_len=r-l+1
            r+=1
        
        return max_len
    
