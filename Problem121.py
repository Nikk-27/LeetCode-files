#Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_index = 0

        for sell_index in range(len(prices)):
            # sell index is always increasing step
            # buy index is increasing only if next one is max profit
            sell_price = prices[sell_index]
            buy_price = prices[buy_index]
            profit = sell_price - buy_price
            if ( profit > max_profit):
                max_profit = profit
            if ( profit < 0):
                buy_index = sell_index
        return max_profit
    
# Example usage:
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(prices))