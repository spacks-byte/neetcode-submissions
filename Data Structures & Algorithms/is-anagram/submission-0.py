class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds = sorted(s)
        sortedt = sorted(t)
        if sorteds == sortedt:
            return True
        else:
            return False
        