class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            left = i+1
            right = len(nums) -1
            target = -nums[i]
            while left < right:
                if right == i:
                    right -= 1
                    continue
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] == target:
                    result.append(tuple(sorted([-target, nums[left], nums[right]])))
                    left += 1
        final = set(result)
        finalList = [list(entry) for entry in final]
        return finalList


        
