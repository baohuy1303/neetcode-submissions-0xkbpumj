class Solution:
    def rob(self, nums: List[int]) -> int:
       # 2 arrs and run on those
       # top down 22 mins
       # bottom up tabulation (12 mins)

        def bottom_up(arr):
            prev, cur = 0, 0
            for num in arr:
                new_max = max(num + prev, cur)
                prev = cur
                cur = new_max
            return cur

        return max(nums[0], bottom_up(nums[1:]), bottom_up(nums[:-1]))
                
                