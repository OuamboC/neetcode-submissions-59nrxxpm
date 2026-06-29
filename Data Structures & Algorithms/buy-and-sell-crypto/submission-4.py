class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start high so any real price beats it immediately
        running_min = float('inf')
        # Set max_profit to 0
        max_profit = 0
        for price in prices:
            # Always holds the cheapest buy price available before today
            running_min = min(price, running_min)
            # Track the profit made
            profit = price - running_min
            # Store the best profit seen so far
            max_profit = max(profit, max_profit)
        return max_profit

        