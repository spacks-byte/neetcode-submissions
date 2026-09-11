class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        if len(tokens) == 0:
                return 0

        stack = deque()

        for entity in tokens:
            match entity:
                case '+':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first+second)
                case '-':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first-second)
                case '*':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first*second)
                case '/':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first/second))
                case _:
                    stack.append(int(entity))
        return stack[0]
        