class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        current_streak = 0
        longest_streak = 0
        for n in numset:
            if n-1 not in numset:
                current_streak = 1
                while n+1 in numset:
                    current_streak+=1
                    n+=1
                if current_streak > longest_streak:
                    longest_streak = current_streak
        return longest_streak
                    
                




            