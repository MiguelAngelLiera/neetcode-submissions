class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,0,1,2], 0, 4
        self.quickSort(nums, 0, len(nums))

    def quickSort(self, nums: List[int], lo, hi) -> None:
        N = hi - lo
        # 4 - 0 = 4
        if N < 2:
            return
        # [1,0,1,2], 0, 4
        # [1,0,1,2], 0, 3
        pivot = self.partition(nums, lo, hi)

        self.quickSort(nums, lo, pivot) # [1,0,1,2], 0, 3,   [0, 1, 1, 2] 1
        self.quickSort(nums, pivot+1, hi) 

    
    def partition(self, nums: List[int], lo, hi) -> int:
        pivot = nums[hi-1] # 2
        i = lo-1 # -1

        for j in range(lo, hi-1): # j in [0, 4]
            if nums[j] < pivot:
                i += 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        

        i += 1
        tmp = nums[i]
        nums[i] = pivot
        nums[hi-1] = tmp

        return i
        