class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        length = len(nums)
        l = 0
        r = k - 1

        final = []

        currentNums = deque()

        for num in nums[l:r+1]:
            currentNums.append(num)

        largestAppended = max(currentNums)

        while r < length-1:
            final.append(largestAppended)
            l+=1
            r+=1
            gone = currentNums.popleft()
            newnum = nums[r]
            currentNums.append(newnum)
            if (newnum > largestAppended):
                largestAppended = newnum 
            else:            
                if gone == largestAppended:
                    largestAppended = max(currentNums)
        final.append(largestAppended)
        return final
            

        
        