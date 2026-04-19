class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if heads < tail, then in original order => return [0]
        # find inflection point where i > i + 1 if heads > tail
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than the rightmost element, 
            # the minimum must be to the right of mid.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is at mid or to the left.
            else:
                r = mid
                
        return nums[l]