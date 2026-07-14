# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        
        # Find mid
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Cut 2 halves from mid
        print(slow.val)
        prev = None
        cur = slow.next
        slow.next = None

        # This cut ensures that 1st half will always be
        # longer or same length

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        final = prev
        cur = head

        while final:
            temp = cur.next
            cur.next = final
            temp_2 = final.next
            final.next = temp
            cur = temp
            final = temp_2
        
        return