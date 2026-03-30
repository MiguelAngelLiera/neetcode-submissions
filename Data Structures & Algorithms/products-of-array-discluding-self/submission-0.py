class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 1
        a, b = [], []
        res = []
        n = len(nums)
        for e in nums:
            m = m * e
            a.append(m)
        r_nums = nums[::-1]
        m = 1
        for e in r_nums:
            m = m * e
            b.append(m)
        b = b[::-1]
        for i in range(n):
            _a = a[i-1] if i > 0 else 1
            _b = b[i+1] if i < n-1 else 1
            res.append(_a * _b)
        return res

        