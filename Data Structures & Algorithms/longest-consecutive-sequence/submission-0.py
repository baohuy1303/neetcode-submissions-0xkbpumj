class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            curLen = 1
            if num - 1 in seen:
                continue
            newNum = num + 1
            while newNum in seen:
                curLen += 1
                newNum += 1
            longest = max(curLen, longest)

        return longest