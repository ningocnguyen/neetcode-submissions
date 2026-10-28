from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # optimized binary search: O(nlogn) time
        # nums = [9, 1, 4, 2, 3, 3, 7]
        # x=9: tails = [9]
        # x=1: tails = [1]
        # x=4: tails = [1,4]
        # x=2: tails = [1,2]
        # x=3: tails = [1,2,3]
        # x=3: tails = [1,2,3]
        # x=7: tails = [1,2,3,7]

        tails = []
        for n in nums:
            index = bisect_left(tails, n)
            if index == len(tails):
                tails.append(n)
            else:
                tails[index] = n
        
        return len(tails)
