
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []
        for n in nums:
            count[n] += 1
        
        items = sorted(count.items(), key = lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(items[i][0])

        return res




        
        
