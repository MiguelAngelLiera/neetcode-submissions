class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        N = len(nums)
        k = 0
        while i != N:
            
            j = i+1
            if nums[i] == val:
                while j < N and nums[j] == val:
                    j += 1
                if j == N:
                    nums[i] = '_'
                else:
                    nums[i] = nums[j]
                    while j < N-1:
                        nums[j] = nums[j+1]
                        j+=1
                    nums[j] = '_'
            else:
                k+=1    
            i += 1
        return k
                