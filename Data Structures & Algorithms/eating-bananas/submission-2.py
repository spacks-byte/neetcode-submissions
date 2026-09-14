class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        maximum = max(piles)
        minimum = 1
        length = len(piles)
        rate = maximum
        while minimum < maximum:
            middle = (maximum + minimum) // 2
            tryTimeBest = 0
            for pile in piles:
                tryTimeBest += math.ceil(pile / middle)
            if tryTimeBest <= h:
                if middle < rate:
                    rate = middle
                maximum = middle
            else:
                minimum = middle + 1
        
        return rate