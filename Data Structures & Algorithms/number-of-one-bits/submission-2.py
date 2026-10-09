class Solution:
    def hammingWeight(self, n: int) -> int:
        from functools import reduce
        if n < 2:
            return n
        binar = f"{bin(n)}"[2:]
        return reduce(lambda x, y: int(x) + int(y), binar)
        