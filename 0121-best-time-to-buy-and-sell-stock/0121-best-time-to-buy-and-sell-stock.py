class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        minbuy = prices[0]

        for sell in prices:
            maxp = sell - minbuy
            maxpro = max(maxp, maxpro)
            minbuy = min(sell, minbuy)

        return maxpro

# TC = O(n)
# SC = O(1)
