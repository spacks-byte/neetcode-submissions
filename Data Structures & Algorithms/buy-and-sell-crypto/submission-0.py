class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        maxProfit = 0

        for i, price in enumerate(prices):
            if price < curMin:
                curMin = price
            elif price > curMin:
                maxProfit = max(maxProfit, price - curMin)
        
        return maxProfit

        