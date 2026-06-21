class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.backtrack(nums, target)
        
    def backtrack(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if target < 0:
            return []
        if N == 1:
            if nums[0] == target:
                return [nums[0:1]]
            return [nums[0:1]+r_combination for r_combination in self.backtrack(nums, target - nums[0])]
        combinations = []
        for i, n in enumerate(nums):
            if n == target:
                combinations += [[n]]
            combinations += [[n]+r_combination for r_combination in self.backtrack(nums[i:], target - n)]

        return combinations