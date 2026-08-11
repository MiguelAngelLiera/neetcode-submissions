class Solution:
    def countSeniors(self, details: List[str]) -> int:
        s = 0
        for p in details:
            if int(p[-4:-2]) > 60:
                s+= 1
        return s

        