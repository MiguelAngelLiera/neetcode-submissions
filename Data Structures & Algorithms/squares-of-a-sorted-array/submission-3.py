class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        print(N)
        if N == 1:
            return [nums[0]**2]
        for i in range(1,N):
            if nums[i]*nums[i-1] <= 0:
                break
        
        j = i - 1
        if nums[i]*nums[j] > 0 and nums[i] > 0:
            i = 0
            j = -1
        print(i,j)

        res = []
        while j >= 0 and i < N:
            if abs(nums[j]) > nums[i]:
                res.append(nums[i]**2)
                i += 1
            else:
                res.append(nums[j]**2)
                j -= 1
        while j >= 0:
            res.append(nums[j]**2)
            j -= 1
        while i < N:
            res.append(nums[i]**2)
            i += 1
        return res

        