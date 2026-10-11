class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = [[]]
        
        for num in nums:
            final += [curr + [num] for curr in final]
             
        return final