class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0
        three = 0

        if len(nums) <= 1:
            return 0 if len(nums) < 1 else nums[0]
      
        for address in nums[:-1]:
            new = address + max(one, two)
            one = two
            two = three
            three = new

        final = max(three, two)
        one = 0
        two = 0
        three = 0

        for address in nums[1:]:
            new = address + max(one, two)
            one = two
            two = three
            three = new

        return max(two,three,final)