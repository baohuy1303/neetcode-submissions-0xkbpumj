class Solution:
    def climbStairs(self, n: int) -> int:
        # at each step can either do 1 or 2
        # recurse down based on remaining steps
        ''' memo = {}
        memo[1] = 1
        memo[0] = 1
        def climb(steps):
            if steps in memo:
                return memo[steps]
            memo[steps] = climb(steps - 1) + climb(steps - 2)
            return memo[steps]
        return climb(n) '''

        if n <= 2:
            return n
        dp = [0] * (n+1) # 0 1 2
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
