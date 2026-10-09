class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nbin = 0
        allbin = 0
        for i, n in enumerate(nums):
            nbin = nbin ^ n
            allbin = allbin ^ i
        allbin = allbin ^ (i+1)

        return allbin ^ nbin
