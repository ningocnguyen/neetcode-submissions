class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for n in nums:
            if n in numset:
                return True
            numset.add(n)

        return False
    