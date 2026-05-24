class Solution:
    def jump(self, nums: List[int]) -> int:
        # cur i can jump to j
        # from i to j, identify the number that can give us the next furthest range
        # 2 4 1 1 1 1
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r+1):
                furthest = max(furthest, i + nums[i])
            l = r+1
            r = furthest
            res += 1
        return res