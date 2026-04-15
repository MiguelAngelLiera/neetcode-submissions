class Solution:
    
    def climbStairs(self, n: int) -> int:
        cache = [0,1]
        if n == 0:
            return cache[0]
        if n == 1:
            return cache[1]
        for i in range(2, n+1):
            cache.append(cache[i-1] + max(cache[i-2], 1))

        return cache[n]
        