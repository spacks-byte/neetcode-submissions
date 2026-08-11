class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        totalNums = len(nums)
        for i in range(totalNums):
            current = nums[i]
            newNums = nums[i+1:]
            newLength = totalNums - (i+1)
            for j in range(newLength):
                insiderCurrent = newNums[j]
                if current + insiderCurrent == target:
                    return [i, j+i+1]



