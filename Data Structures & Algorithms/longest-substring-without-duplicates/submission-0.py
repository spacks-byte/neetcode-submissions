class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        charQueue = deque()
        longest = 0
        for char in s:
            if char not in charQueue:
                charQueue.append(char)
            else:
                longest = max(longest, len(charQueue))
                popped = charQueue.popleft()
                while char != popped:
                    popped = charQueue.popleft()
                charQueue.append(char)
        
        return max(longest, len(charQueue))
