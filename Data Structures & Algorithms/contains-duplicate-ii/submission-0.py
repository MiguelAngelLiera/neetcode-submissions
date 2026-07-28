class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        for i in range(N):
            j = 1
            while j <= k and i + j < N:
                if nums[i] == nums[i+ j]:
                    return True
                j += 1
        return False