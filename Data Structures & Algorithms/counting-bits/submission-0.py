class Solution:
    def countBits(self, n: int) -> List[int]:
        final = []
        for i in range(n+1):
            z = i
            ones = 0
            while z > 0:
                ones += z & 1
                z = z >> 1
            final.append(ones)
            
        return final