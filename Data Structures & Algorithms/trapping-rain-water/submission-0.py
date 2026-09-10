class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        l,r = 0,length-1
        total = 0
        lastLVal = height[l]
        lastRVal = height[r]
        lSize=0
        rSize=0

        while l != r:
            if height[l] < height[r]:
                l += 1
                if height[l] > lastLVal:
                    total += lSize
                    lSize = 0
                    lastLVal = height[l]
                else:
                    lSize += lastLVal - height[l]
            else:
                r -= 1
                if height[r] > lastRVal:
                    total += rSize
                    rSize = 0
                    lastRVal = height[r]
                else:
                    rSize += lastRVal - height[r]
        
        return total + rSize + lSize



        