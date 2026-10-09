class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        main = 0
        for num in nums:
            main = main ^ num
        
        return main
        