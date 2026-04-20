class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find inflection point so that we have 2 sorted arrays
        # search on each

        def binarySearch(nums, l, r, target):
            while l <= r:
                mid = (r+l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return binarySearch(nums, l, r, target)

        while l < r:
            mid = (r+l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        pivot = l
        print(pivot)
        if nums[pivot] == target:
            return pivot
        if nums[pivot] < target and target <= nums[-1]:
            return binarySearch(nums, pivot, len(nums) - 1, target)
        else:
            return binarySearch(nums, 0, pivot - 1, target)