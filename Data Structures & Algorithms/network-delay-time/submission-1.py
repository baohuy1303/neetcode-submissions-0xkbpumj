class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}

        for time in times:
            adj[time[0]].append((time[1], time[2]))
        
        minHeap = [(0, k)]
        seen = set()
        res = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in seen:
                continue
            res = t1
            seen.add(n1)
            for n2, t2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(minHeap, (t2 + t1, n2))

        return res if len(seen) == n else -1