class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        streak = 0
        longest = 0
        for n in numSet:
            if n-1 not in numSet:
                streak = 1
                while n+1 in numSet:
                    streak += 1
                    n+=1
                if streak > longest:
                    longest = streak
        return longest
