class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            else:
                if len(stack) <= 0:
                    return False
                
                lastBracket = stack.pop()
                if char != brackets.get(lastBracket, ''):
                    return False
        
        if len(stack) > 0:
            return False
        
        return True

        