import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain max k-len list
        res = []
        for i in range(0, len(nums)):
            heapq.heappush(res, nums[i])
            if len(res) > k:
                heapq.heappop(res)

        return res[0]
