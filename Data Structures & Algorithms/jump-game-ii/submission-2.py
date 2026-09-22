class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        n = len(nums) - 1
        if n == 0:
            return 0
        max_reach = 0
        current_end = 0
        for i, jump in enumerate(nums):
            max_reach = max(i + jump, max_reach)
            if current_end == i:
                jumps+=1
                current_end = max_reach
                if current_end >= n:
                    break
                
        return jumps
