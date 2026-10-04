class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l<r:
            mid = (l+r)//2
            total_hours = sum((p+mid-1)//mid for p in piles)
            if total_hours > h:
                l=mid+1
            else:
                r=mid
        
        return r

