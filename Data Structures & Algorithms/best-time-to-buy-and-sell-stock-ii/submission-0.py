class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1:
            return max_profit
        points= prices[:1]
        for i, p in enumerate(prices[1:], start = 1):
            last = points[-1]
            if p - last > prices[i-1] - last: 
                points.append(last)
            else:
                points.append(p)
                max_profit += prices[i-1] - last
        
        max_profit += prices[-1] - points[-1]

        return max_profit

