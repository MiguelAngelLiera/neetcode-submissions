class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        for _ in s:
            if len(p) == 0 and _ in (')', ']', '}'):
                return False
            if _ == ')':
                if p[-1] == '(':
                    p.pop()
                else:
                    return False
            elif _ == ']':
                if p[-1] == '[':
                    p.pop()
                else:
                    return False
            elif _ == '}':
                if p[-1] == '{':
                    p.pop()
                else:
                    return False
            else:
                p.append(_)
        return len(p) == 0
        