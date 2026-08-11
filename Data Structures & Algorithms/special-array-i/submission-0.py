class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(1, N):
            if nums[i- 1] % 2 == nums[i] % 2:
                return False
        return True
        