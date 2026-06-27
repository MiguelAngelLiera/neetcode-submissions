class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.backtrack(n, k)
    
    def backtrack(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            combinations = []
            for i in range(n, 0, -1):
                combinations.append([i])
            return combinations

        combinations = []
        for i in range(n, 0, -1):
            combinations += [[i] + combination for combination in self.backtrack(i - 1, k - 1)]
        
        return combinations


        