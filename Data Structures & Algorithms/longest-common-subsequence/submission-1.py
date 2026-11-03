class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lenOne = len(text1)+1
        lenTwo = len(text2)+1

        dp = [[0] * lenOne for _ in range(lenTwo)]
        for i in range(1,lenTwo):
            for j in range(1, lenOne):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
            



        