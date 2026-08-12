class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums)

        if N == 1:
            return nums
        if N == 2:
            if nums[0] > nums[1]:
                return [nums[1], nums[0]]
                return nums
        mid = N // 2
        left = self.sortArray(nums[mid:])
        right = self.sortArray(nums[:mid])
        return self.mergeSorted(left, right)

    def mergeSorted(self, a: List[int], b: List[int]) -> List[int]:
        i = 0
        N = len(a)
        while i < N and b:
            if a[i] > b[0]:
                tmp = b.pop(0)
                a[:] = a[:i] + [tmp] + a[i:]
                N += 1
            i += 1
        if b:
            a[:] = a[:] + b[:]
        return a
            

