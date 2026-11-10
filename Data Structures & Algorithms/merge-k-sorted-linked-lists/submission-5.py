# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode(0)
        for i in range(len(lists)):
            if not lists[i]:
                continue

            heapq.heappush(heap, [lists[i].val, i, lists[i]])
        
        cur = res
        while heap:
            val, i, node = heapq.heappop(heap)
            nxt = node.next
            cur.next = node
            cur = cur.next
            if nxt:
                heapq.heappush(heap, [nxt.val, i, nxt])

        return res.next