class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        count={}
        freq_max=0
        l=0

        for r in range(len(s)):
            char=s[r]
            count[char]=count.get(char,0)+1
            if freq_max < count[char]:
                freq_max = count[char]
            
            if r-l+1 - (freq_max) > k:
                count[s[l]]-=1
                l+=1

            if res < (r-l+1):
                res = r-l+1
        return res