class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak=0
        current_streak=0
        numset=set(nums)

        for n in numset:
            if n-1 not in numset:
                current_streak=1
                while n+1 in numset:
                    current_streak+=1
                    n+=1
                if longest_streak<current_streak:
                    longest_streak=current_streak
        
        return longest_streak
            

            