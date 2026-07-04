class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = [0]
        lookup = set(nums)
        memo = {}

        def dfs(num):
            if num not in lookup:
                return 0
            if num in memo:
                return memo[num]

            length = dfs(num + 1)
            memo[num] = 1 + length
            res[0] = max(1 + length, res[0])
            return 1 + length
        
        for num in nums:
            dfs(num)
        
        return res[0]