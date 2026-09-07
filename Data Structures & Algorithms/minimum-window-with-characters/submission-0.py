class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        have=0
        countT={}
        window={}
        l=0
        res=[-1, -1]
        reslen = float("inf")

        for i in t:
            countT[i]=countT.get(i,0)+1
        need=len(countT)

        for r in range(len(s)):
            char=s[r]
            window[char]=window.get(char,0)+1
            if char in t and window[char]==countT[char]:
                have+=1

            while need==have:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                left_char=s[l]
                window[left_char]-=1
                l+=1
                if left_char in t and window[left_char]<countT[left_char]:
                    have-=1
        l, r = res
        return s[l:r+1]
        
        
        
        
        
        
        