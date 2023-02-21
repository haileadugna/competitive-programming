# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        slow, cur = dummy, head
        for _ in range(left - 1):
            slow = slow.next
            cur = cur.next
        
        
        pres = None
        for i in range(right - left + 1):
            nxt= cur.next
            cur.next = pres
            pres = cur
            cur = nxt
        
        slow.next.next = cur
        slow.next = pres
        return dummy.next
        
        
       
            
        
        
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        