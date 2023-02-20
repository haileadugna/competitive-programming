# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        is_cycle = False
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast is slow:
                return True

        return False
                
                
# a = ListNode(3)
# b = ListNode(2)
# c = ListNode(0)
# d = ListNode(-4)

# a.next = b
# b.next = c
# c.next = d
# d.next = b
                
                
            
            
        