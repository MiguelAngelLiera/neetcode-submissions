class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        i = 0
        f = 1
        while f < len(prices):
            profit = prices[f] - prices[i]
            if profit > max_p:
                max_p = profit
            if prices[f] < prices[i]:
                i = f
            f += 1
        return max_p