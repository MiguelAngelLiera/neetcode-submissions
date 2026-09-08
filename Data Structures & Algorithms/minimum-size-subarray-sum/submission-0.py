class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1]+n)
        #prefix.pop(0)
        #print(prefix)
        i = 1
        j = 0
        enough = False
        min_l = float('inf')
        while i < N+1:
            if prefix[i] - prefix[j] >= target:
                enough = True
                min_l = min(min_l, i - j)
                j += 1
            else:
                enough = False
                i += 1
        
        if min_l == float('inf'):
            return 0
        return min_l
