class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = {}
        for char in t:
            chars[char] = chars.get(char, 0) + 1

        lengthOfSegment = len(t)
        length = len(s)
        l,r = 0, lengthOfSegment - 1
        currentBest = ""

        requiredMatches = len(chars)
        matches = 0

        total = {}
        for char in s[l:r+1]:
            total[char] = total.get(char, 0) + 1

        for key in chars.keys():
            if total.get(key, 0) >= chars[key]:
                matches += 1

        while r < length:
            if matches == requiredMatches:
                if (r - l + 1) < len(currentBest) or currentBest == "":
                    currentBest = s[l:r+1]
                if s[l] in chars and total[s[l]] == chars[s[l]]:
                    matches -= 1
                total[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < length:
                    total[s[r]] = total.get(s[r], 0) + 1
                    if s[r] in chars and total[s[r]] == chars[s[r]]:
                        matches += 1
        return currentBest