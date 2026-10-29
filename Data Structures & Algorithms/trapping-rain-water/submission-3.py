class Solution:
    def trap(self, height: List[int]) -> int:
        # amount of water is governed by max of left and right
        # find the max left and max right at each position
        # left prefix array and right suffix array
        # time: O(n), space: O(n)

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        water = 0

        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water

        # height=[2,1,0,1,2] --> 0+1+2+1 = 4
        # max_left = [2, 2, 2, 2, 2]
        # max_right = [2, 2, 2, 2 ,2]

        # height=[0,2,0,3,1,0,1,3,2,1]
        # max_left = [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        # max_right = [3,3,3,3,3,3,3,3,2,1]
        # water = 0+0+2+0+2+3+2+0+0=9



        