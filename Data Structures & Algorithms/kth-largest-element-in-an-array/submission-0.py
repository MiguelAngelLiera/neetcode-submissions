
import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            hq.heappush(h, -n)

        while k:
            last = hq.heappop(h)
            k -= 1
        
        return -last