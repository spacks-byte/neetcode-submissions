class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [1] * m

        for y in range(1,n):
            for x in range(1,m):
                dp[x] = dp[x] + dp[x-1]

        return dp[-1]