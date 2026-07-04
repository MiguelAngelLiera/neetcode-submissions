class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        N = len(nums2)
        i= 0
        j = 0
        #if m == 0:
        #    for i, n in enumerate(nums2):
        #        nums1[i] = n
        while j < N and i < len(nums1):
            if i == m:
                for k, n in enumerate(nums2[j:]):
                    nums1[i+ k] = n
            if nums2[j] < nums1[i]:
                a = nums2[j]
                t = i
                while i <= m:
                    nums1[i] = nums1[i] + a
                    a = nums1[i] - a
                    nums1[i] = nums1[i] - a
                    i += 1
                i = t + 1
                j += 1
                m += 1
            else:
                i += 1


        