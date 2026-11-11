class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        countT = Counter(t)
        need = len(countT)
        min_len = float('inf')
        res = [-1, -1]

        l,r = 0, 0
        countS = defaultdict(int)
        for r in range(len(s)):
            countS[s[r]] += 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have+=1
            
            while need == have:
                # store index l and r
                if min_len > (r-l+1):
                    min_len = r-l+1
                    res = [l, r]

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1

        l,r = res
        return s[l:r+1]

