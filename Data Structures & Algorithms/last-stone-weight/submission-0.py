class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=stones
        n=len(stones)

        for i in range(n):
            heap[i]=-heap[i]

        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap,stone1 - stone2)
        
        if len(heap) == 1:
            return -heap[0]
        return 0