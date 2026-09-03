class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        buildingNums = sorted(list(set(nums)))
        longestSoFar = 0
        currentLength = 1
        for i in range(1, len(buildingNums)):
            if buildingNums[i] == (buildingNums[i-1] + 1):
                currentLength += 1
            else:
                if currentLength > longestSoFar:
                    longestSoFar = currentLength
                    currentLength = 1
                else:
                    currentLength = 1
        
        if currentLength > longestSoFar:
            return currentLength
        return longestSoFar

        