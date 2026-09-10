class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sortedNums = list(sorted(nums))
        
        for i in range(len(sortedNums)):
            left = i+1
            right = len(sortedNums) -1
            target = -sortedNums[i]
            while left < right:
                if right == i:
                    right -= 1
                    continue
                if sortedNums[left] + sortedNums[right] < target:
                    left += 1
                elif sortedNums[left] + sortedNums[right] > target:
                    right -= 1
                elif sortedNums[left] + sortedNums[right] == target:
                    result.append(tuple(sorted([-target, sortedNums[left], sortedNums[right]])))
                    left += 1
        final = set(result)
        finalList = [list(entry) for entry in final]
        return finalList


        
