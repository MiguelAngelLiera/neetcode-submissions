class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*(2*n)
        for i, e in enumerate(nums):
            ans[i] = e
            ans[n+i] = e

        return ans
        