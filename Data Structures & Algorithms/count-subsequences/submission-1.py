class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s)+1) for _ in range(len(t))]
        dp.append([1] * (len(s)+1))
        
        
        for i in range(len(t)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                if s[j] == t[i]:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
        
        return dp[0][0]