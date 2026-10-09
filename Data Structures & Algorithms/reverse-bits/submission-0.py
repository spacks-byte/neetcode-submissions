class Solution:
    def reverseBits(self, n: int) -> int:
        final = 0
        for i in range(32):
            final = final << 1
            if n & 1:
                final = final | 1
            n = n >> 1
        return final
        