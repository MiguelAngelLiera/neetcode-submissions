class Solution:
    from collections import defaultdict
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for k, v in d.items():
            if v > N / 2:
                return k
        return k


        