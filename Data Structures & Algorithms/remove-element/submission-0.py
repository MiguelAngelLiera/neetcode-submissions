class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        #j = i + 1
        N = len(nums)
        k = 0
        while i != N:
            
            j = i+1
            if nums[i] == val:
                k += 1
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
                
            i += 1
        print(nums)
        return N - k
                