class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            total = currentSum + num
            if total < num:
                total = num
            
            if total > maxSum:
                maxSum = total
                currentSum = total
            else:
                currentSum = total
            
        return maxSum