import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(0, len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            x = -(heapq.heappop(stones))
            y = -(heapq.heappop(stones))
            if x == y:
                continue
            if x > y:
                heapq.heappush(stones, -(x-y))
            
        return -stones[0] if len(stones) > 0 else 0
