''' array nums

return the length of the LONGEST strictly increasing subsequence

subsequence: a sequence that has holes, char delete, but follows order

STRICTLY INCREASING: > no >=

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

brute-force: try to match a number with every single next number -> O(n!)

unsorted so
at each index, for loop to see if valid to explore
max(1 + dfs(valid_index))

 '''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return 1
            if i in memo:
                return memo[i]
            length = 0
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                length = max(dfs(j), length)
            memo[i] = length+1
            return length + 1
        res = 0
        for i in range(len(nums)):
            res = max(dfs(i), res)
        return res
