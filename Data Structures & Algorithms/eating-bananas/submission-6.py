from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speeds = (1, max(piles)+1)
        return self.aux_minEatingSpeed(piles, h,speeds)
    
    def aux_minEatingSpeed(self, piles: List[int], h: int, speeds: Tuple[int]) -> int:
        N = speeds[-1] - speeds[0]
        if N == 1:
            return speeds[0]

        if self.evaluate_k(speeds[0] + N//2, piles) > h:
            return self.aux_minEatingSpeed(piles, h, (speeds[0] + N//2 + 1, speeds[-1]))
        if self.evaluate_k(speeds[0] + N//2, piles) <= h:
            if self.evaluate_k(speeds[0] + N//2 - 1, piles) > h:
                return speeds[0] + N//2
            else:
                return self.aux_minEatingSpeed(piles, h, (speeds[0], speeds[0] + N//2))


    def evaluate_k(self, k_hat, piles):
        cumulate_h = 0
        for p in piles:
            if k_hat >= p:
                cumulate_h += 1
            else:
                cumulate_h += ceil(p / k_hat)
        return cumulate_h