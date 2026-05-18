class Solution:
    def rob(self, nums: List[int]) -> int:
       # 2 arrs and run on those
       # top down 22 mins
       # bottom up

        def bottom_up(arr):
            dp = [0] * (len(arr) + 1)
            dp[0] = 0
            dp[1] = arr[0]
            for i in range(2, len(arr) + 1):
                dp[i] = max(dp[i-1], arr[i-1] + dp[i-2])
            return dp[len(arr)]
        if len(nums) == 1:
            return nums[0]
        return max(bottom_up(nums[1:]), bottom_up(nums[:-1]))
                
                