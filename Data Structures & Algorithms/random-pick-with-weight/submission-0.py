class Solution:

    def __init__(self, w: List[int]):
        # [1,3,2]
        # [1] [2,3,4] [5,6]
        # create prefix array: [1,4,6]
        # binary search to find index: target = rand from 1-6 
        # find index of the first element that is greater than / equal to target

        self.prefix_sum = []
        self.current = 0
        for n in w:
            self.current += n
            self.prefix_sum.append(self.current)

    def pickIndex(self) -> int:
        target = random.randint(1, self.current)
        l, r = 0, len(self.prefix_sum)-1

        while l<=r:
            mid = (l+r) // 2
            if target <= self.prefix_sum[mid]:
                r=mid-1
            else:
                l=mid+1
        
        return l
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()