class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        middle = 0

        while left < right:
            middle = (left + right) // 2
            midValu = nums[middle]
            leftValu = nums[left]
            rightValu = nums[right]
            if target == midValu:
                return middle
            if rightValu > leftValu:
                if target < midValu:
                    right = middle
                else:
                    left = middle + 1
            else:
                # num right < num left
                if midValu >= leftValu and midValu >= rightValu:
                    if target >= midValu:
                        left = middle + 1
                    elif target >= leftValu:
                        right = middle
                    else:
                        left = middle + 1
                if midValu <= leftValu and midValu <= rightValu:
                    if target <= midValu:
                        right = middle
                    elif target <= rightValu:
                        left = middle + 1
                    else:
                        right = middle

        middle = (left + right) // 2
        if target == nums[middle]:
            return middle

        return -1
       