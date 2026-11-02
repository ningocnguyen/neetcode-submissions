class Solution:
    def trap(self, height: List[int]) -> int:
        # T: O(n)
        # S: O(n)
        # water is governed by min of max left and max right
        n = len(height)
        max_l = [0] * n
        max_l[0] = height[0]
        max_r = [0] * n
        max_r[n-1] = height[n-1]
        # left max at idx i
        for i in range(1, n):
            max_l[i] = max(height[i], max_l[i-1])
        # right max at idx i
        for i in range(n-2, -1, -1):
            max_r[i] = max(max_r[i+1], height[i])

        water = 0
        for i in range(n):
            water += min(max_l[i], max_r[i]) - height[i]
        return water


        
