class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] is length longest increasing subsequence ending at i
        # dp[i] is max of dp[i] and dp[j] (any nums at index j where nums[j] < nums[i])
        # dp[i] = max(dp[i], dp[j]+1)

        n = len(nums)
        dp = [1] * (n)
        for end in range(1,n):
            for start in range(end):
                if nums[start] < nums[end]:
                    dp[end] = max(dp[end], dp[start]+1)
        
        return max(dp)
                


