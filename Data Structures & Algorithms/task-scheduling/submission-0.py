import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # most freq task and track when can process again.
        # most freq task gonna help minimize

        # each time: check if queue[0] time has come, add to heap
        # process most freq, record time + n and add to queue, pop the most freq

        # q: [[freq, time]]

        # get freq
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]

        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
            if max_heap:
                cur = 1 + heapq.heappop(max_heap)
                if cur != 0:
                    q.append([cur, time + n + 1])
            
        
        return time
