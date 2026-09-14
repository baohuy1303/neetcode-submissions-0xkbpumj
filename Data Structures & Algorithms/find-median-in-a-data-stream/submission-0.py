class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        l = self.left_max_heap
        r = self.right_min_heap

        if l and num > -l[0]:
            heapq.heappush(r, num)
        else:
            heapq.heappush(l, -num)

        if len(r) > len(l) + 1:
            heapq.heappush(l, -heapq.heappop(r))
        elif len(l) > len(r) + 1:
            heapq.heappush(r, -heapq.heappop(l))
        return

    def findMedian(self) -> float:
        l = self.left_max_heap
        r = self.right_min_heap

        if len(r) > len(l):
            return r[0]
        elif len(l) > len(r):
            return -l[0]
        
        return (-l[0] + r[0]) / 2
        
        