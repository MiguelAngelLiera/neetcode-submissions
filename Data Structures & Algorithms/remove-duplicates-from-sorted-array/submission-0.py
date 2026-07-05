class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1
        duplicates = 0
        i = 0
        j = 1
        while j < N:
            while j< N and nums[i] == nums[j]:
                j += 1
                duplicates += 1
            if j < N:
                nums[i+1] = nums[j]
            i += 1
            j += 1

        return N - duplicates 

        