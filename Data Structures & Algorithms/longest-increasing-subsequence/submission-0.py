class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = 1

        for first in range(length):
            cur = nums[first]
            curMax = 0
            for second in range(first):
                if nums[second] < cur:
                    if dp[second] > curMax:
                        curMax = dp[second]
            dp[first] = curMax + 1

        return max(dp)

