class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        f = n
        while abs(i - f) > 1:
            n_ = len(nums[i:f])
            mid = int((i + f)/2)
            if nums[mid] > target:
                f = mid
            elif nums[mid] < target:
                i = mid
            else:
                return mid
        if nums[i] == target:
            return i
        else:
            return -1
        return -1
