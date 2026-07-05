class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        N = len(nums)
        while j < N:
            if nums[j] != 0:
                t = nums[j]
                nums[j] = 0
                nums[i] = t
                j += 1
                i += 1
            else:
                while j < N and nums[j] == 0:
                    j += 1
                
        