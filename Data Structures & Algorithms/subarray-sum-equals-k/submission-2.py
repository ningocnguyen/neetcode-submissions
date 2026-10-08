class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = 0
        res = 0

        for n in nums:
            curr_sum += n
            res += prefix_sum[curr_sum-k] # defaultdict --> empty evaluates to 0
            prefix_sum[curr_sum] += 1

        return res