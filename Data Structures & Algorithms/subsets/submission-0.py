class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.aux_subsets([], set(nums))
            
    
    def aux_subsets(self, base, nums):
        subsets = [base]
        visited = set()
        for n in nums:
            visited.add(n)
            new_base = base.copy()
            new_base.append(n)
            subsets += self.aux_subsets(new_base, nums - visited)
            
        return subsets
