import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-n for n in nums]
        hq.heapify(self.nums)
        

    def add(self, val: int) -> int:
        hq.heappush(self.nums, -val)
        tmp = self.nums[:]
        #print(self.nums)
        for i in range(self.k):
            res = hq.heappop(self.nums)
        
        self.nums = tmp[:]
        return -res
        
        
