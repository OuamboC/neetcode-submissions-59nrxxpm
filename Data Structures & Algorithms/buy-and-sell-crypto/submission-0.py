class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_min = float('inf')
        max_profit = 0
        for price in prices:
            running_min = min(price, running_min)
            profit = price - running_min
            max_profit = max(profit, max_profit)
        return max_profit

        