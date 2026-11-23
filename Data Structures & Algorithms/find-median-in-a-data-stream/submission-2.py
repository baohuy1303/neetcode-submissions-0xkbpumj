class MedianFinder:

    def __init__(self):
        self.left = [] # max-heap
        self.right = [] # min-heap


    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))

        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)

        if total % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        
        return -self.left[0]
        