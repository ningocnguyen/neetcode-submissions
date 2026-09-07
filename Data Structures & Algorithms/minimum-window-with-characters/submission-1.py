class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        r,l = 0, 0
        countT = {}
        window = {}
        resLen = float('inf')
        res = [-1,-1]

        for char in t:
            countT[char] = countT.get(char,0)+1

        need = len(countT)

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while need == have:
                if resLen > (r-l+1):
                    resLen = r-l+1
                    res = [l,r]
                char = s[l]
                window[char] -= 1
                l+=1
                if char in countT and window[char] < countT[char]:
                    have -= 1

        l,r = res
        return s[l:r+1]
                