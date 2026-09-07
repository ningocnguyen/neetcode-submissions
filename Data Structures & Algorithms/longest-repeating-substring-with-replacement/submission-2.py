class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        freq_max=0
        l=0
        count={}
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            freq_max=max(freq_max,count[s[r]])
            while (r-l+1)-freq_max > k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res