class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        streak = 0
        longest = 0
        for n in nums:
            if n-1 not in numset:
                streak = 1
                while n+1 in numset:
                    streak+=1
                    n+=1
                if longest < streak:
                    longest = streak

        return longest

            

                


