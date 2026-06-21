class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = self.backtrack(nums)
        new_subsets =[]
        for s in subsets:
            if s:
                s.sort()
            new_subsets.append(tuple(s))
        new_subsets = set(new_subsets)

        # subsets =set([tuple(s.sort()) for s in subsets ])
        return [list(s) for s in new_subsets]

    def backtrack(self, nums):
        N = len(nums)
        if N == 0:
            return [[]]
        if N == 1:
            return [nums[0: 1], []]
        subsets = []
        for i, n in enumerate(nums):
            ssub = self.backtrack(nums[i+1:])
            t = [[n]+sub for sub in ssub]
            t = t + ssub
            subsets += t
        return subsets
            

        