
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = defaultdict(int)
        for n in nums:
            numDict[n] += 1
        
        heap = []
        for n, i in numDict.items():
            heapq.heappush(heap, (i,n))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]