# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode(0)
        cur = res
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(heap, [lists[i].val, i, lists[i]])

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if not node:
                continue
            heapq.heappush(heap, [node.val, i, node])
        
        return res.next