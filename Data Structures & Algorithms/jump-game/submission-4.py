class Solution:
    def canJump(self, nums: List[int]) -> bool:

        i = len(nums) - 1
        goal = i

        while i >= 0:
            total = nums[i] + i
            if total >= goal:
                goal = i
            i -= 1 
        
        if goal == 0:
            return True
        return False