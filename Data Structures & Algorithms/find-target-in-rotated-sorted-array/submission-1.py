class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        pivot = self.search_pivot(nums, (0, N))

        f_idx = self.binary_search(nums, target, (0, pivot+1))
        s_idx = self.binary_search(nums, target, (pivot+1, N))

        if f_idx != -1:
            return f_idx
        if s_idx != -1:
            return s_idx

        return -1
    

    def search_pivot(self, nums: List[int], bounds: Tuple[int]) -> int:
        i, j = bounds
        N = j - i
        
        if N == 1:
            return i
        if nums[j-1] >= nums[i+N//2] > nums[i]:
            return j-1
        if nums[i+N//2] > nums[i] > nums[j-1]:
            return self.search_pivot(nums, (i+N//2, i+N))
        if nums[i] > nums[j-1] >= nums[i+N//2]:
            return self.search_pivot(nums, (i, i+N//2))


    def binary_search(self, nums: List[int], target: int, bounds: Tuple[int]) -> int:
        i, j = bounds
        N = j - i
        if N == 0:
            return -1
        if N == 1:
            return i if nums[i] == target else -1
        
        mid = i + N // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binary_search(nums, target, (mid, i+N))
        if nums[mid] > target:
            return self.binary_search(nums, target, (i, mid))