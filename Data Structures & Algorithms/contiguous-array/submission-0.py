class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            # treat 0 as -1 and 1 as +1
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in first_seen:
                max_len = max(max_len, i - first_seen[prefix_sum])
            else:
                first_seen[prefix_sum] = i

        return max_len
