class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset = collections.defaultdict(lambda: 0)
        numAndCount = []

        for num in nums:
            numset[num] = numset[num] + 1
        
        for (num, repetitions) in numset.items():
            numAndCount.append((repetitions, num))

        interestingNums = sorted(numAndCount, reverse=True)[:k]
        justNums = [numberAndCount[1] for numberAndCount in interestingNums]
        return justNums
