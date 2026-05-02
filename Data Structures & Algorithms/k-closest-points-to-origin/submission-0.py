import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # compute out into a dist list
        # min_heap, pop k times

        dist = []
        res = []
        for point in points:
            cur = math.sqrt( (point[0])**2 + (point[1])**2 )
            dist.append(tuple([cur, point]))

        heapq.heapify(dist)
        while k > 0:
            res.append(heapq.heappop(dist)[1])
            k -= 1

        return res
