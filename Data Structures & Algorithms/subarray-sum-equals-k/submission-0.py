class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        # Base case: a prefix sum of 0 has occurred once (represents an empty prefix)
        prefix_counts[0] = 1

        curr_sum = 0
        total_count = 0

        for num in nums:
            curr_sum += num

            # If (curr_sum - k) exists, those previous prefixes form valid subarrays ending at the current index
            total_count += prefix_counts[curr_sum - k]

            # Record the current prefix sum
            prefix_counts[curr_sum] += 1

        return total_count