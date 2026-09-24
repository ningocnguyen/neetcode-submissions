class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_func(houses: List[int]) -> int:
            rob1, rob2 = 0, 0
            for money in houses:
                current = max(money+rob2, rob1)
                rob2 = rob1
                rob1 = current
            
            return current
        
        return max(rob_func(nums[1:]), rob_func(nums[:-1]))
