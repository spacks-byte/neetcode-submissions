class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearedString = "".join(x.lower() for x in s if (x!=" " and x.isalnum()))
        return clearedString == clearedString[::-1]
        