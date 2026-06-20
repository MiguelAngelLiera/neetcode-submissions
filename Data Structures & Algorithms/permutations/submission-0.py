class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        return self.backtrack(nums)


    def backtrack(self, nums):
        
        N = len(nums)
        if N == 1:
            return [nums[0:1]]
        permutations =[]
        for i, n in enumerate(nums):
            remain = nums[:i] + nums[i+1:]
            permutations += [[n] + r_permutation for r_permutation in self.backtrack(remain)]
        return permutations

        