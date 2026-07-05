""" list of heights -> len n

find 2 lines that form a container that contains the max water
return max water

brute-force: from each line, end with every other line, record max found
-> O(n^2)

how do we form a container and water volume?
    - water volume: shortest height * (dist from i til ending line)
    - same for container

were always limited by shortest height -> need to find a pair that maximizes the height * dist
we can try the longest dist 1st then start shrinking to find max height

start 0, n
calculate max_volume at each pair. shrink (l += 1, r -= 1) whichever side is lower so we can try to find
a new bound

-> O(n) """
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        res = 0

        while l < r:
            cur = min(heights[l], heights[r]) * (r-l)
            res = max(res, cur)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res