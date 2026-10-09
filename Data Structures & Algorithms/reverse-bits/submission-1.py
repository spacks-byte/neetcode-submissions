class Solution:
    def reverseBits(self, n: int) -> int:
        final = 0
        for i in range(32):
            if n & 1:
                final |= 1 << 31-i
            n = n >> 1
        return final
        