class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        mem = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    mem[i] = max(mem[i], mem[j]+1)
        
        mlen = 1
        for m in mem:
            if m > mlen:
                mlen = m
        
        return mlen

        