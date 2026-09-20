class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [-1] * (n+1)
        dp[1] = nums[0]
        dp[2] = max(dp[1], nums[1])

        for i in range(3, n+1):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])

        return dp[n]