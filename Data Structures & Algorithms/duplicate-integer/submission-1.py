class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        currentVal = 0
        nums.sort()
        for i in nums:
            if currentVal == i:
                return True
                break
            else:
                currentVal = i
        return False