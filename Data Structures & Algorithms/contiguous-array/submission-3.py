class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # prefix sum hash map
        max_len = 0
        bal = 0
        first = {0: -1}

        for i, n in enumerate(nums):
            bal += 1 if n == 1 else -1

            if bal in first:
                max_len = max(max_len, i - first[bal])

            else:
                first[bal] = i

        return max_len


