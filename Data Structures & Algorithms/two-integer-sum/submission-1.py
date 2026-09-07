class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mynums = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in mynums:
                return [mynums[diff],i]
            mynums[n] = i

