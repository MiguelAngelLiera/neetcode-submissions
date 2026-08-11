class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        s = 0
        prev = float('inf')
        for n in nums:
            if n <= prev:
                s = n
            else:
                s += n
            max_sum = max(s, max_sum)
            prev = n
        return max_sum 
        