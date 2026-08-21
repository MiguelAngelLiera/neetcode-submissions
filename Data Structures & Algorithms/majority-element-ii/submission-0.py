from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        times = len(nums) // 3
        res = []
        for n, t in c.items():
            if t > times:
                res.append(n)
        return res

        