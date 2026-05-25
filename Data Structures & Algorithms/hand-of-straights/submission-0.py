import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = Counter(hand)
        heap = list(freq.keys())
        heapq.heapify(heap)
        while heap:
            start = heap[0]
            for i in range(groupSize):
                cur = start + i
                print(cur)
                if freq[cur] == 0:
                    return False
                freq[cur] -= 1
                if freq[cur] == 0:
                    if cur != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True
