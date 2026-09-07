class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        max_heap=[]

        for x,y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(max_heap,(distance,[x,y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        for pair in max_heap:
            res.append(pair[1])
        
        return res