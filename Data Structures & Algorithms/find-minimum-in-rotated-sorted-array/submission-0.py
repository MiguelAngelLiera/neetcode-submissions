class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        i = nums[0]
        j = nums[-1]
        mid = nums[N//2]
        if N//2 + 1 < N and mid > nums[N//2 + 1]:
            return nums[N//2 + 1]
        if N//2 -1 > -1 and mid < nums[N//2 -1]:
            return mid
        if mid > j:
            return self.findMin(nums[N//2:])
        if mid < i:
            return self.findMin(nums[:N//2])
        return nums[0]
        