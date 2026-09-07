class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        l=0
        r=len(heights)-1
        while l<r:
            current_area=min(heights[l],heights[r])*(r-l)
            if current_area>max_area:
                max_area=current_area
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_area