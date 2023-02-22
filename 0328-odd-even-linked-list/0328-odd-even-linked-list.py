# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        fast = head
        odd = cur = head
        even = cur2 = head.next
        while fast and fast.next != None and fast.next.next != None:
            fast = fast.next.next
            cur.next = fast
            cur = cur.next 
            cur2.next = fast.next
            cur2 = cur2.next
        cur.next = even
        return odd