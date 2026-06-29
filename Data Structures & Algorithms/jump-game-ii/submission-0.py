class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        N = len(nums)
        steps = 0
        while i < N- 1:
            j = nums[i]

            if j == 0:
                break

            steps += 1
            if i + j>= N - 1:

                break
            maxstep = i + 1
            maxval = nums[maxstep] - j + 1
            for idx in range(i+2, i+j+1):
                if nums[idx] - j + idx - i > maxval:
                    maxstep = idx
                    maxval = nums[idx] - j + idx - i
            print(maxstep)
            i = maxstep
        
        return steps
                
        