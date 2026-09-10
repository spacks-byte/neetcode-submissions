class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        l, r = 0, length-1
        currentMaxVol = 0
        while l < r:
            maxVol = (r-l)*min(heights[l], heights[r])
            currentMaxVol = max(currentMaxVol, maxVol)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return currentMaxVol
            

        