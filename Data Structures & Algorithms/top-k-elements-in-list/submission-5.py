
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        res = []
        for n in nums:
            count[n] += 1
        
        for n, i in count.items():
            heapq.heappush(heap, (i,n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for item in heap:
            res.append(item[1])

        return res