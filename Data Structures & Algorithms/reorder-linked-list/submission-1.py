# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
            
        if head.next.next is None:
            return
        
        # Find mid
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(node):
            
            return prev # final node
        
        # Reverse from mid
        slow = slow.next
        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        final = prev
        cur = head

        while final and final.next:
            temp = cur.next
            cur.next = final
            temp_2 = final.next
            final.next = temp
            cur = temp
            final = temp_2
        
        return