class Solution:
    def trap(self, height: List[int]) -> int:
        # compute max prefix and max suffix 
        # prefix, suffix: each index gonna keep max until find new max, just starts from diff dir

        """
        To solve this, we first need to figure out what makes up the trapped rain at a certain area.
        First intuition was to see if left > right, if so then add water in
        But trapped means left and right the highest of everything in between.
        A trapped water at a pos is determined by their left highest and right highest.
        Water only flows to lowest one so we know we're trapped by the lowest on each.
        Then we need to subtract our cur_height to get the water amount.
        Keep track of left_highest and right_highest for each with prefix and suffix
        Then add area for each with formula
        """

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
