class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset = {}
        numAndCount = []

        for num in nums:
            if num in numset:
                numset[num] = numset[num] + 1
            else:
                numset[num] = 1
        
        for (num, repetitions) in numset.items():
            numAndCount.append((repetitions, num))

        interestingNums = sorted(numAndCount, reverse=True)[:k]
        justNums = [numberAndCount[1] for numberAndCount in interestingNums]
        return justNums
