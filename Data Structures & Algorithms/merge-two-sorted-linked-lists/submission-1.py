# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2

        if p1 is None and p2 is None:
            return None

        if not p1 and p2:
            return p2
        elif not p2 and p1:
            return p1

        dummy = ListNode()
        cur = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next

        if p1 and not p2:
            cur.next = p1
        elif p2 and not p1:
            cur.next = p2
        
        return dummy.next