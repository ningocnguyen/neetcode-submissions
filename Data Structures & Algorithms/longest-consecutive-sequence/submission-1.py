class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak=0
        num_set=set(nums)
        for n in num_set:
            if n-1 not in num_set:
                current_streak=1
                while n+1 in num_set:
                    current_streak+=1
                    n+=1
                if longest_streak<current_streak:
                    longest_streak=current_streak
        return longest_streak
                    



            