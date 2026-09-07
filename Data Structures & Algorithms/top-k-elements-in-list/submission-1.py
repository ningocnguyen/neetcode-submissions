from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        res = []

        for n,i in count.items():
            heapq.heappush(heap,(i,n))
            if len(heap) > k:
                heapq.heappop(heap)

        for item in heap:
            res.append(item[1])

        return res