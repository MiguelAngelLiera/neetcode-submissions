class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, elem in enumerate(nums):
            dif = target - elem
            if dif in m.keys():
                return [m[dif], i]
            m[elem] = i 
            
        