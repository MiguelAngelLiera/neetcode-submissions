class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] <= 0:
                del nums[i]
                N -= 1
            else:
                i += 1
        print(nums)
        nums = list(set(nums))
        nums.sort()
        s = 1
        for i, n in enumerate(nums):
            if n != i+ 1:
                return s
            s += 1  
        return s
        