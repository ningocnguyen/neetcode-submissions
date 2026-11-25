class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        max_len = 0
        first_seen = {0: -1}  

        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1

            if balance in first_seen:
                max_len = max(max_len, i - first_seen[balance])
            else:
                first_seen[balance] = i

        return max_len