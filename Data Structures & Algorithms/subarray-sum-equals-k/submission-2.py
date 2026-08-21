from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        p_sum = 0
        res = 0
        for n in nums:
            p_sum += n 
            if p_sum == k:
                res += 1
        
            c=sums[p_sum-k]
            if c:
                res += c
            sums[p_sum] += 1
        return res
                    


        