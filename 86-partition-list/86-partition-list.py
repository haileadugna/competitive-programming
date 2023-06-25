# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_head = ListNode(0)
        less = less_head
        great_head = ListNode(0)
        great = great_head
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            
            else:
                great.next = head
                great = great.next
            head = head.next
            
        # Connect the end of the "less" list to the start of the "great" list
        less.next = great_head.next
        great.next = None
        # print(great)
        return less_head.next