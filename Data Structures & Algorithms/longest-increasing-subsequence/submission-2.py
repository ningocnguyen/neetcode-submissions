class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] is length LIS of array ending at index i
        # dp[i] tracks the max of the subsequence ending at the index before i and dp[i]
        #-> we can append nums[i] to whatever subsequence ending at nums[j] where nums[j] < nums[i]
        # formula: dp[i] = max(dp[i], dp[j]+1)
        n = len(nums)
        dp = [1] * n
        if not nums:
            return 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)