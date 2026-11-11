class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        count = defaultdict(int)
        curr = 0
        n = len(nums)
        l = 0

        # for i in range(k):
        #     count[nums[i]] += 1
        #     curr += nums[i]
        # if len(count) == k:
        #     max_sum = max(max_sum, curr)

        for i in range(n):
            count[nums[i]] += 1
            curr += nums[i]

            if i-l+1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                curr -= nums[l]
                l+=1

            if len(count) == k:
                max_sum = max(max_sum, curr)

        return max_sum
