class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        max_l = height[l]
        max_r = height[r]
        water = 0

        while l<r:
            if max_l < max_r:
                l+=1
                max_l = max(max_l, height[l])
                water += max_l - height[l]
            else:
                r-=1
                max_r = max(max_r, height[r])
                water += max_r - height[r]

        return water
            

