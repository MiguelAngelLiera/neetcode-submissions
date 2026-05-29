class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        if len(nums) == 0 and target is not None:
            return idx
        return self.aux_searchInsert(nums, target, idx)

    def aux_searchInsert(self, nums: List[int], target: int, idx: int) -> int:
        N = len(nums)
        m = N // 2
        
        if N == 1:
            if nums[0] < target:
                return idx + 1
            # elif nums[0] > target:
            #     return idx - 1
            else:
                return idx
        if nums[m] < target:
            return self.aux_searchInsert(nums[m:], target, idx+m)
        elif nums[m] > target:
            return self.aux_searchInsert(nums[:m], target, idx)
        else:
            return idx+m

        

        