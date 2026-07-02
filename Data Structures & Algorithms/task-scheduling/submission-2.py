import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get all freq
        # we always want to process the max_freq first
        # because they will bottleneck later on

        # letter doesnt really matter so we just need
        # the number of freq for x amount of tasks
        # max_heap to always process the max_freq
        # need a queue because if use only max_heap cases such as:
        # A: 3, B:1, C:1 would fail because A:2 would still be in front
        
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]

        q = deque() # (cur_freq, time_process)
        heapq.heapify(max_heap)
        time = 0
        while max_heap or q:
            time += 1
            if q and q[0][1] == time:
                cur, time = q.popleft()
                heapq.heappush(max_heap, cur)

            if max_heap:
                cur = 1 + heapq.heappop(max_heap)
                if cur != 0:
                    q.append((cur, time + n + 1))
        
        return time

        