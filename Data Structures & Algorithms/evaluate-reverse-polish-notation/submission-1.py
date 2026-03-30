class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                if len(stack) < 2:
                    return None
                right = stack.pop()
                left = stack.pop()
                res = int(eval(f"{left}{token}{right}"))
                stack.append(res)
            else:
                stack.append(token)
        return int(stack.pop())