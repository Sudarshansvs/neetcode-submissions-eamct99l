class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 101
        for i in range(len(prices)-1):
            buy = min(buy, prices[i], prices[i+1])
            profit = max(profit, prices[i+1]-buy)
        return profit