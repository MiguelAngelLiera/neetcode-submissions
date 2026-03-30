class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        L = 0

        mL = 0
        mR = 1

        for R in range(1, len(nums)+1):
            curSum += nums[R-1]

            if maxSum < curSum:
                maxSum = curSum
                mL = L
                mR = R
            
            if curSum < 0:
                curSum = 0
                L = R

        return sum(nums[mL:mR])
        