''' O(n) just return min

we need to find the point of separation?

base: if [0] < [-1] then its the orginal pos and just return [0]

we just find the place where left > right (which means we found the separation between
the 2 sorted partitions) we just return right?

how do we know when to go right or left
    - compare left, right with mid:
        + left < mid -> sorted
        + right > mid -> sorted
        + left > mid -> unsorted
        + right < mid -> unsorted

if both sorted just return left
how do we determine which is our target?
if mid_n > r_n means we cant consider mid as a min: l = mid + 1
if mid_n < l_n means we still consider mid as a min: r = mid

 '''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (r+l) // 2
        while l < r:
            mid = (r+l) // 2
            ln = nums[l]
            rn = nums[r]
            mn = nums[mid]
            if ln < mn and rn > mn:
                return ln
            if ln >= mn:
                r = mid
            if rn < mn:
                l = mid + 1

        return nums[l]
        