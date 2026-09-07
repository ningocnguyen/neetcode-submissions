class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        # max heap
        heapq.heappush(self.small,-num)

        val=-heapq.heappop(self.small)
        # min heap
        heapq.heappush(self.large,val)

        if len(self.large) > len(self.small):
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-val)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return -self.small[0]
        