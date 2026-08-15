import functools

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        possiblenums = {}
        zeroes = nums.count(0)
        if zeroes > 1:
            return [0] * len(nums)
        if zeroes == 1:
            results = [0] * len(nums)
            index = nums.index(0)
            newnums = nums[:index] + nums[index+1:]
            product = functools.reduce(lambda x,y: x*y,newnums)
            results[index] = product
            return results
        
        for i, num in enumerate(nums):
            if num in possiblenums:
                results.append(possiblenums[num])
            else:
                newnums = nums[:i] + nums[i+1:]
                product = functools.reduce(lambda x,y: x*y,newnums)
                results.append(product)
                possiblenums[num] = product
        return results