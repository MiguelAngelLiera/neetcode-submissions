class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        m = [0, cost[-1]]
        n = len(cost)
        if n==1:
            return m[1]
        for i in range(n-2, -1, -1):
            m.append(cost[i] + min(m[-1], m[-2]))
        
        return min(m[-1], m[-2])
        