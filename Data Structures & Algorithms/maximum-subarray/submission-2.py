class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for i in range(len(nums)):
            total = currentSum + nums[i]
            if total < nums[i]:
                total = nums[i]
            
            if total > maxSum:
                maxSum = total
                currentSum = total
            else:
                currentSum = total
            
        return maxSum