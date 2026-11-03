class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # length k
        # distinct values
        # sliding window

        count = defaultdict(int)
        max_sum = 0
        curr = 0
        n = len(nums)

        for i in range(k):
            count[nums[i]] += 1
            curr += nums[i]

        if len(count) == k:
            max_sum = max(max_sum, curr)

        for i in range(k, n):
            count[nums[i]] += 1
            curr += nums[i]
            out = nums[i-k]
            count[out] -= 1
            curr-=out
            if count[out] == 0:
                del count[out]
            if len(count) == k:
                max_sum = max(curr, max_sum)


        return max_sum


 