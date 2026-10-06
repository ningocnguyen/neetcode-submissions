class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        res = 0

        for n in nums:
            curr_sum += n
            res += prefix_counts[curr_sum-k]
            prefix_counts[curr_sum] += 1

        return res