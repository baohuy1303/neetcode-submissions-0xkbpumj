class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in numSet:
                return [numSet[diff], i]
            numSet[n] = i

                
        