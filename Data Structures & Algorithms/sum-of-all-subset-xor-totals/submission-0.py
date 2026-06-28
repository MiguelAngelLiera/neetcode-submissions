class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = self.backtrack(nums)
        print(subsets)
        sum_ = 0
        for s in subsets:
            xor = 0
            for e in s:
                xor = xor ^ e
            sum_ += xor

        return sum_            

    
    def backtrack(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if not N:
            return [[]]
        subsets = []
        ssub = self.backtrack(nums[1:])
        subsets += ssub
        subsets += [nums[0:1] + sub for sub in ssub]

        return subsets

        