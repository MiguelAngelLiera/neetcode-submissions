import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [- s for s in stones]
        hq.heapify(stones)
        while len(stones) > 1:
            first = hq.heappop(stones)
            second = hq.heappop(stones)
            res = abs((-first) - (-second))
            if res > 0:
                hq.heappush(stones, -res)
        if not stones:
            return 0
        return -stones[0]