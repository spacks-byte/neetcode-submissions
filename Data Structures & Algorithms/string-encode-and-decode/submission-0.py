class Solution:

    def encode(self, strs: List[str]) -> str:
        finalstr = ""
        for word in strs:
            finalstr += (f"{len(word)}#{word}")
        return finalstr


    def decode(self, s: str) -> List[str]:
        listofstrs = []
        index = 0
        totallength = len(s)
        segmentlength = 0
        while index < totallength:
            if s[index] == '#':
                index += 1
                listofstrs.append(s[index:index+segmentlength])
                index += segmentlength
                segmentlength = 0
            else:
                segmentlength = (segmentlength * 10) + int(s[index])
                index += 1

        return listofstrs


