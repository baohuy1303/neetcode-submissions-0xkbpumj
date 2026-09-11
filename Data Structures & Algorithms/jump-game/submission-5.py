class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = nums[0]
        i = 0
        while i <= res:
            res = max(res, i + nums[i])
            if res >= len(nums) - 1:
                return True
            i += 1

        if res >= len(nums) - 1:
            return True
            
        return False