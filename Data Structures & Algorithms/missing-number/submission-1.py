class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        XOR = 0
        for i in range(0, len(nums) + 1):
            XOR = XOR ^ i
        
        for i in range(0, len(nums)):
            XOR = XOR ^ nums[i]
        
        return XOR