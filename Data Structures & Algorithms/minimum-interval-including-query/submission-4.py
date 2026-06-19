''' integer array intervals, where intervals[i] = [left_i, right_i] INCLUSIVE

array of query points queries
queries[j] return shortest interval such that left_i <= queries[j] <= right_i
if no such exist, return -1

return output[j] is the result of query[j].

for each query, we need to find an interval that can contain the query number, and is also the smallest
out of all the valid intervals

find valid intervals, and find the smallest one

M: len intervals, N: len queries
brute-force: O(M * N) - for each query, go thru every interval, see if valid and update the smallest one?

how can we know which interval is valid?
    - line sweep? --1----2-----3------6-------7
    only store openings and map that to the length. so a number only needs to go until it reaches its max opening
    stop when num < cur_opening (and skip when cur_opening + length < num)
    but this worst-case would be O(M) too
    
    how do we sort and bin-search for the min length based on the number to optimize time better?

    or we keep track of intervals with a heap?
 '''
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)

        sorted_queries = [0] * len(queries)
        for i in range(len(queries)):
            sorted_queries[i] = [queries[i], i]
        sorted_queries.sort(key=lambda x: x[0])

        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heapify(heap)
        cur = 0

        for q, i in sorted_queries:
            while cur < len(intervals) and intervals[cur][0] <= q:
                # push (len, closing_bracket)
                heapq.heappush(heap, ( intervals[cur][1] - intervals[cur][0] + 1, intervals[cur][1] ) )
                cur += 1

            while len(heap) > 0 and heap[0][1] < q:
                heapq.heappop(heap)

            if len(heap) == 0:
                res[ i ] = -1
            else:
                res[ i ] = heap[0][0]
            
        return res






