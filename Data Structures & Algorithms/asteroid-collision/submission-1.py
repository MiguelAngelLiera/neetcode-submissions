class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while a < 0 and s and s[-1] > 0:
                b = s.pop()
                if abs(b) == abs(a):
                    break
                if abs(b) > abs(a):
                    s.append(b)
                    break
            else:
                s.append(a)
        return s
        