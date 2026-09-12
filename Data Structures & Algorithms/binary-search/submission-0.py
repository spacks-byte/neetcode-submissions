class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = -1
        left = 0
        right = len(nums)
        
        while left < right:
            middle = left + (( right - left )//2)
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle
        return -1   