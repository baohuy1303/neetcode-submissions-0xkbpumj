from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])
        
        lookup = defaultdict(int)
        lookup[0] = 1
        res = 0
        for prefix in prefix_sum:
            if prefix - k in lookup:
                res += lookup[prefix-k]
            lookup[prefix] += 1
        return res
