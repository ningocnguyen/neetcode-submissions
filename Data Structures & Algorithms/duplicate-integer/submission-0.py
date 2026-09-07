class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mylist=set()
        for n in nums:
            if n in mylist:
                return True
            mylist.add(n)

        return False