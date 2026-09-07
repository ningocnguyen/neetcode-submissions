class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        most=0
        longest=0
        l=0
        r=0

        for r in range(len(s)):
            char=s[r]
            count[char]=count.get(char,0)+1
            if most<count[char]:
                most=count[char]
            while (r-l+1)-most>k:
                count[s[l]]-=1
                l+=1
            if longest<(r-l+1):
                longest=r-l+1

        return longest




        