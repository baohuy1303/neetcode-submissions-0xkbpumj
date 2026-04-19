class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if heads < tail, then in original order => return [0]
        # find inflection point where i > i + 1 if heads > tail
        # go mid, check if mid > pointer left: left is large group
        # if mid < pointer left: means left is small group
        l = 0
        r = len(nums) - 1
        
        mid = 0
        while l < r:
            mid = (r + l) // 2
            if nums[l] < nums[r]:
                return nums[l]
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid

        return nums[r]