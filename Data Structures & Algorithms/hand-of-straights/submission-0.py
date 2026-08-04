from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        d = defaultdict(list)
        if N % groupSize != 0:
            return False
        hand.sort()
        pos = [1]*N
        for i, e in enumerate(hand):
            d[e].append(i)
        print(d)
        
        for i, e in enumerate(hand):
            print(pos)
            if pos[i] != groupSize:
                next_ = d.get(e+1, None)
                if next_:
                    j = d[e+1].pop(0)
                    pos[j] = pos[i] + 1
                else:
                    return False
        return True


            

        