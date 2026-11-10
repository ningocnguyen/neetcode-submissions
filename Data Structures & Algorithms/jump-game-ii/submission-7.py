class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        reach = 0
        curr_end = 0
        n=len(nums)-1
        if n==0:
            return 0
        for i, jump in enumerate(nums):
            reach = max(i+jump, reach)
            
            if i == curr_end:
                jumps+=1
                curr_end = reach
                if reach>=n:
                    break

        return jumps

            


