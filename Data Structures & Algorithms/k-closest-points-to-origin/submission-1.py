import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # compute out into a dist list k times
        # max_heap, check first element, if smaller then we can pop and push in
        # this reduces n + n + k*logn to n*logk

        dist = []
        i = 0
        while i < k:
            point = points[i]
            cur = math.sqrt( (point[0])**2 + (point[1])**2 )
            heapq.heappush(dist, tuple([-cur, point]))
            i += 1
        
        while i < len(points):
            point = points[i]
            cur = math.sqrt( (point[0])**2 + (point[1])**2 )
            if cur < -dist[0][0]:
                heapq.heappop(dist)
                heapq.heappush(dist, tuple([-cur, point]))
            i += 1

        res = []
        for coord in dist:
            res.append(coord[1])
        return res
