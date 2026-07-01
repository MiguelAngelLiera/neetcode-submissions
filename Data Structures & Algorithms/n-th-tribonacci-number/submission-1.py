class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        mem = [0, 1, 1]
        while n-2:
            mem.append(mem[-1]+mem[-2]+mem[-3])
            n -= 1
        
        return mem[-1]
        