"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # overlap gets new room
        # have a heap of rooms, with the min end time at front
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda x: x.start)
        heap = [intervals[0].end]
        heapq.heapify(heap)
        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappushpop(heap, intervals[i].end)
            else:
                heapq.heappush(heap, intervals[i].end)

        return len(heap)
        