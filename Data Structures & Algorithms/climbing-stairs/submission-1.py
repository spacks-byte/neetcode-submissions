class Solution:
    def climbStairs(self, n: int) -> int:
        one = 0
        two = 1

        if n <= 1:
            return 1
      
        for i in range(n):
            new = one + two
            one = two
            two = new

        return two
        