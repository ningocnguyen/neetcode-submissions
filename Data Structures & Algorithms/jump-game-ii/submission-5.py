class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy
        # track current position's reach: find furthest reach in that i+j range
        # increment jumps if finish 1 level: i+j jumps

        current_end = 0
        furthest = 0
        n = len(nums)
        if n == 1:
            return 0
        jumps = 0

        for i in range(n):
            furthest = max(furthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = furthest
                if current_end >= (n-1):
                    break

        return jumps