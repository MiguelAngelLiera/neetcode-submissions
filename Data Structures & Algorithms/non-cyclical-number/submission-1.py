class Solution:
    def isHappy(self, n: int) -> bool:
        next_ = self.check_digits(n)
        h = set()
        while next_ != 1:
            print(next_)
            if next_ in h:
                return False
            h.add(next_)
            next_ = self.check_digits(next_)
        return True



    def check_digits(self, n: int) -> int:
        strn = str(n)
        s = 0
        for d in strn:
            s += int(d)**2
        return s
        