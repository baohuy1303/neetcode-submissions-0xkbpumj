''' 0 <= k <= 1000

k linked lists

number of nodes = k * 100 = 100,000 = n

return the smallest starting node

Brute force: O(nlogn)

get smallest element on all of them at each iteration
    - have pointers on all of them - k pointers. compare the pointers, once we have the smallest one
    attach it to our res and move the pointer up on the linkedlist. compare repeatedly until all the linkedlists
    have pointers at the end. O(n*k)

    - push k linkedlist values into a min-heap (val, address to node)
        + iterate thru all nodes and push O(nlogk)

 '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        res = ListNode(0)
        cur = res

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            val, i, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            node.next = None
            cur.next = node
            cur = cur.next
        
        return res.next










