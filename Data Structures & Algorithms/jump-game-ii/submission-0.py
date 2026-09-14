class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # exhausted the range of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # early exit if our next jump can already reach the end
                if current_end >= n - 1:
                    break

        return jumps