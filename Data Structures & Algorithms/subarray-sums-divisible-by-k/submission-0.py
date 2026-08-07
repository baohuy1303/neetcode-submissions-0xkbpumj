class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])
        print(prefix_sum)
        # num % k == 0
        # if remainder in lookup then we add
        lookup = defaultdict(int)
        lookup[0] = 1
        res = 0
        for prefix in prefix_sum:
            if prefix % k in lookup:
                print(prefix)
                res += lookup[prefix%k]
            lookup[prefix%k] += 1
        return res