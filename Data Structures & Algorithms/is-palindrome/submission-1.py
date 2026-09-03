class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearedString = "".join(filter(lambda x : (x!=" " and x.isalnum()), s.lower()))
        return clearedString == clearedString[::-1]
        