class Solution:

    def __init__(self, w: List[int]):
        # [1,3,2]
        # [1,4,6]
        # keep an array of running sum
        self.prefix_sum = []
        self.curr = 0
        for n in w:
            self.curr += n
            self.prefix_sum.append(self.curr)

    def pickIndex(self) -> int:
        pick = random.randint(1, self.curr) # random from 1-6
        # binary search to find the smallest number in range that random pick belongs
        l, r = 0, len(self.prefix_sum)-1
        while l<=r:
            mid = (l+r)//2
            if pick == self.prefix_sum[mid]:
                return mid
            elif pick < self.prefix_sum[mid]:
                r=mid-1
            else:
                l=mid+1
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()