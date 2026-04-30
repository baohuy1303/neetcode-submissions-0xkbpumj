import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # build max heap
        self.k = k
        for i in range(0, len(nums)):
            nums[i] = -nums[i]
        print(nums)
        heapq.heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        cur = self.nums.copy()
        print(cur)
        k = self.k
        res = 0
        while k > 0:
            res = heapq.heappop(cur)
            k -= 1
        return -res

        

