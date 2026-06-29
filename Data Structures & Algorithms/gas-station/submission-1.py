class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g - c for g, c in zip(gas,cost)]
        if sum(diff) < 0:
            return -1
        total = 0
        res = 0
        for i, d in enumerate(diff):
            total += d
            if total < 0:
                total = 0
                res = i+1
        return res

