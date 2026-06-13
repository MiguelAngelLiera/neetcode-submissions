class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t_numbers = set([])
        for i in nums:
            if i in t_numbers:
                return i
            t_numbers.add(i)

        