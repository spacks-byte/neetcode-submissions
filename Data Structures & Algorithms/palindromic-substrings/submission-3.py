class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        total = 0

        def expand(left, right) -> int:
            count = 0
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    return count
                count += 1
                left -= 1
                right += 1
            return count

        for y in range(length):
            if y < length - 1:
                if s[y] == s[y+1]:
                    total += expand(y, y+1)
            total += expand(y, y)

        return total
