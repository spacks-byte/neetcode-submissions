class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds = sorted(s)
        sortedt = sorted(t)
        return sorteds == sortedt
        