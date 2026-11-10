class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            cur_visible = 0

            while stack and stack[-1] <= height:
                stack.pop()
                cur_visible += 1

            if stack:
                cur_visible += 1

            res[i] = cur_visible
            stack.append(height)

        return res
            