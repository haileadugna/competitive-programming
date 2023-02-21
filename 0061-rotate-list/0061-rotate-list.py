# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        if k > cnt :
            k = k % cnt
        if k == 0:
            return head
            
        n = k
        fast = head
        while k > 0:
            fast = fast.next
            k -= 1
            
        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
         
        rest = slow
        while slow.next:
            slow = slow.next

        cur = head
        l = cnt - n 
        while l > 0:
            slow.next = ListNode(cur.val)
            slow = slow.next
            cur = cur.next
            l -= 1
 
        return rest
        
        