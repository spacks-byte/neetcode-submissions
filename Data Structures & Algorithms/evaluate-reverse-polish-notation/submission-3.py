class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        if len(tokens) < 3:
            if len(tokens) == 0:
                return 0
            else:
                return int(tokens[0])

        stack = []
        operators = ['+', '-', '*', '/']

        for entity in tokens:
            if entity in operators:
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
            else:
                stack.append(int(entity))
        return stack.pop()
        