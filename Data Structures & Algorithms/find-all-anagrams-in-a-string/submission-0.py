class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        res = []
        if m<n:
            return []
        # return starting indices
        l=0
        countP = Counter(p)
        count = defaultdict(int)
        for r in range(n):
            count[s[r]] += 1
            if count == countP:
                res.append(r-n+1)

        for r in range(n, m):
            count[s[r]] += 1
            count[s[l]] -= 1
            if count[s[l]] == 0:
                del count[s[l]]
            l+=1
   
            if count == countP:
                res.append(r-n+1)

        return res
        



