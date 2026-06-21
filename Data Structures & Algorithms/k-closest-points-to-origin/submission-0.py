import heapq as hq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        closest = []
        for x, y in points:
            hq.heappush(h, (self.euclidean(x, y), (x, y)))

        while k:
            d, (x, y) = hq.heappop(h)
            closest.append([x, y])
            k -= 1
        
        return closest


    def euclidean(self, x, y):
        return sqrt((x - 0)**2 + (y - 0) **2)

        