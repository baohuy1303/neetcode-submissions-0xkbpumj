class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # go backwards
        # keep track of index that jumps to end
        # ask can reach end? then can reach cur?
        n = len(nums) - 1
        cur = n
        print(cur)
        for i in range(len(nums) - 1, -1, -1):
            print(cur)
            if nums[i] + i >= n:
                cur = i
            else:
                if nums[i] + i >= cur:
                    cur = i
        
        if cur <= 0:
            return True
        return False
            