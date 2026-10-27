class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        current = 0
        res = 0

        for n in nums:
            current += n
            diff = current - k
            if diff in prefix:
                res += prefix[diff]
            prefix[current] = prefix.get(current, 0) + 1
        
        return res