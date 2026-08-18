class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        memo = {}
        def recursion(i):
            if i in memo:
                return memo[i]

            cur_len = 1

            for j in range(i + 1, n):
                if nums[j] <= nums[i]:
                    continue
                cur_len = max(recursion(j) + 1, cur_len)
            memo[i] = cur_len
            return cur_len

        for i in range(0, n):
            res = max(res, recursion(i))
        return res