class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        most=0
        count={}
        longest=0

        for r in range(len(s)):
            char=s[r]
            count[char]=count.get(char,0)+1
            if most < count[char]:
                most=count[char]

            if (r-l+1)-most > k:
                count[s[l]]-=1
                l+=1

            if longest<(r-l+1):
                longest=r-l+1
        
        return longest
