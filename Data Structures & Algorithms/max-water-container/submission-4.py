class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l = 0
        r = len(heights) - 1
        current = 0

        while l < r:
            current = min(heights[l], heights[r]) * (r-l)
            if maxW < current:
                maxW = current
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return maxW
        
        
