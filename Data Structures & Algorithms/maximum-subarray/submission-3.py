class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum+num)
            max_sum = max(current_sum, max_sum)

        return max_sum