# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
            
        ind = length // 2
        
        curr = head
        
        while curr and ind > 0:
            curr = curr.next
            ind -= 1
        
        return curr
        
        
        
        
#         slow = head
#         fast = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
            
#         return slow