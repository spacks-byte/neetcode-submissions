class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = 0
        two = 0

        if len(cost) <= 1:
            return 0
      
        for stairCost in cost:
            new = stairCost + min(one, two)
            one = two
            two = new

        return one if one < two else two
        