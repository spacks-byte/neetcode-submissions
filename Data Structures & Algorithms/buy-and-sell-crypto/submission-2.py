class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        maxProfit = 0

        for price in prices:
            if price < curMin:
                curMin = price
            else:
                maxProfit = max(maxProfit, price - curMin)
        
        return maxProfit

        