class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap
        res = []
        heap = []
        for x,y in points:
            heapq.heappush(heap,(-(x**2+y**2),[x,y])) # tuple
            if len(heap) > k:
                heapq.heappop(heap)

        for pair in heap:
            res.append(pair[1])

        return res


        
