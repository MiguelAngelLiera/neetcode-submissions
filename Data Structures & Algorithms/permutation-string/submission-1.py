class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N = len(s1)
        M = len(s2)
        if N > M:
            return False
        for i in range(M-N+1):
            if self.verify_sub(s1, s2[i:i+N]):
                return True
        return False

    def verify_sub(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2):
            return False
        frecs2 = dict.fromkeys(s2, 0)
        frecs1 = dict.fromkeys(s1, 0)
        for s in s1:
            frecs1[s] += 1
        for z in s2:
            frecs2[z] += 1
        return frecs1 == frecs2
            

        