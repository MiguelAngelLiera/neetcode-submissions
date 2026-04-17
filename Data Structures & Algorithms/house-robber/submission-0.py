class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
    #     l1 = nums[0] + self.rob(nums[2:])
    #     l2 = nums[1] + self.rob(nums[3:])
    #     return max(l1, l2)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c = [0,0, nums[0]]
        n = len(nums)
        for i in range(1,n):
            l1 = nums[i] + c[-2]
            l2 = nums[i-1] + c[-3]
            c.append(max(l1, l2))
        return c[-1]
        