class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # given all the nums in the array will be [1, n]
        # all the num values will be within the index of the array
        # so we can use the value/number as an index to travel/check
        # because the same numbers will give back the same index.

        res = 0
        for i in range(0, len(nums)):
            cur_val = abs(nums[i])
            if nums[cur_val] < 0:
                return cur_val
            else:
                nums[cur_val] = -(nums[cur_val])