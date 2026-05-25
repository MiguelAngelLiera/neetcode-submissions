class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for operation in logs:
            if operation == "../":
                if stack > 0:
                    stack -= 1
                else:
                    pass
            elif operation == "./":
                pass
            else:
                stack += 1
        return stack

        