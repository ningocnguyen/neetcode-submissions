class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # longest subarray with sum = 0
        max_len = 0
        count = {0: -1}
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum += 1 if n == 1 else -1
            if curr_sum in count:
                max_len = max(max_len, i-count[curr_sum])

            else:
                count[curr_sum] = i

        return max_len

