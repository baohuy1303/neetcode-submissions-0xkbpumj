# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        dummy = ListNode()
        dummy.next = head

        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1

        i = 0
        cur = dummy
        while i < length - n:
            cur = cur.next
            i += 1

        cur.next = cur.next.next
        return dummy.next