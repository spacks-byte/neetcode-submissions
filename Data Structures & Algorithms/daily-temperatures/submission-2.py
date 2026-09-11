class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        final = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                popped = stack.pop()
                final[popped] = i - popped
                
            stack.append(i)

        return final
            
        

        