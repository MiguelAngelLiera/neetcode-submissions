class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        add = []
        for i in range(n-k+1):
            add.append(max(nums[i:i+k]))
        return add