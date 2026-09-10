class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        smolLen = len(s1)
        length = len(s2)
        newSOne = str(sorted(s1))

        l,r = 0, smolLen-1

        while r < length:
            window = str(sorted(s2[l:r+1]))
            if newSOne == window:
                return True
            else:
                l+=1
                r+=1
        return False