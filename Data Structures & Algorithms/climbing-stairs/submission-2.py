class Solution:
    def climbStairs(self, n: int) -> int:
        # at each step can either do 1 or 2
        # recurse down based on remaining steps
        memo = {}
        memo[1] = 1
        memo[0] = 1
        def climb(steps):
            if steps in memo:
                return memo[steps]
            memo[steps] = climb(steps - 1) + climb(steps - 2)
            return memo[steps]
        return climb(n)