class Solution:
    D = set([str(i) for i in range(10)])
    def decodeString(self, s: str) -> str:
        N = len(s)
        i = 0
        res = ''
        while i < N:
            c = s[i]

            if c in self.D:
                d = i
                while s[d] in self.D:
                    d += 1
                a = int(s[i: d])
                i = d - 1
                j = 1
                stack = [s[i+j]]
                while stack:
                    j += 1
                    if s[i+j]== '[':
                        stack.append('[')
                    elif s[i+j]== ']':
                        stack.pop()

                sub = self.decodeString(s[i+2: i+j])
                res += a*sub
                i += j + 1

            else:
                res += s[i]
                i += 1
        return res 




        