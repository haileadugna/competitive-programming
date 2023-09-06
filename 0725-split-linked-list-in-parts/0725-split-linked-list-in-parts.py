# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        cur = head
        
        while cur:
            cur = cur.next
            length += 1
            
        
        curr = head
        avg = length// k
        res = []
        mod = length% k
        
        for i in range(k):
            
            write = ListNode(None)
            head = write
            
            if mod > 0:
            
                for j in range(avg + 1):
                    write.next = write = ListNode(curr.val)
                    if curr:
                        curr = curr.next
                        
                mod -= 1
            else:
                for j in range(avg):
                    write.next = write = ListNode(curr.val)
                    
                    if curr:
                        curr = curr.next
   
            res.append(head.next)
        
        return res