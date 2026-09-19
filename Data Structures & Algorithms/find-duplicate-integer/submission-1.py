class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        i = 0

        while True:
            if i in seen:
                return i
            seen.add(i)
            cur = nums[i]
            i = cur
        