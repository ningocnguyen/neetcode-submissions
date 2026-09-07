
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        count={}

        for n in nums:
            count[n]=count.get(n,0)+1
        
        item_list=list(count.items())
        item_list=sorted(item_list,key=lambda x:x[1],reverse=True)

        for i in range(k):
            res.append(item_list[i][0])

        return res

    