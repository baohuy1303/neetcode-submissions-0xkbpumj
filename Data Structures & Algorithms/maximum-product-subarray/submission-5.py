class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = 1
        cur_min = 1
        res = nums[0]
        for num in nums:
            cur_max, cur_min = max(num, cur_max*num, cur_min*num), min(num, cur_max*num, cur_min*num)
            res = max(cur_max, res)
        return res