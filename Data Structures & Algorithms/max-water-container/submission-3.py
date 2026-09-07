class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        l=0
        r=len(heights)-1

        while l<r:
            current=min(heights[l], heights[r])*(r-l)
            if max_water<current:
                max_water=current
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return max_water
