class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0

        for y in range(length):
            for x in range(y+1, length+1):
                sub = s[y:x]
                if sub == sub[::-1]:
                    count += 1

        return count