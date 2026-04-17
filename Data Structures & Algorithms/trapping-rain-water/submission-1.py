class Solution:
    def trap(self, height: List[int]) -> int:
        # compute max prefix and max suffix 
        # prefix, suffix: each index gonna keep max until find new max, just starts from diff dir

        prefix = [0] * len(height)
        suffix = [0] * len(height)
        cur_max = 0
        for i in range(0, len(height)):
            cur_max = max(height[i], cur_max)
            prefix[i] = cur_max
        cur_max = 0

        for i in range(len(height) - 1, -1, -1):
            cur_max = max(height[i], cur_max)
            suffix[i] = cur_max
            
        area = 0
        for i in range(0, len(height)):
            area += max(0, min(prefix[i], suffix[i]) - height[i])

        return area
