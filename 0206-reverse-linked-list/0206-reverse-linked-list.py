# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        newNode = None
        while cur:
            prev = newNode
            newNode =  ListNode(cur.val)
            newNode.next = prev
            cur =  cur.next
            
        return newNode
