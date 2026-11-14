class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # number of bananas each time: [1,4]
        l,r = 1, max(piles)
        while l<r:
            mid = (l+r)//2
            total_hours = sum((p+mid-1)//mid for p in piles)
            if total_hours <= h:
                r=mid
            else:
                l=mid+1

        return l