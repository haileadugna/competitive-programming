# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)
    
    def merge(self, left, right):
        temp = ListNode()
        node = temp
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
                
            else:
                node.next = right
                right = right.next
                
            node = node.next
        node.next = left or right
        return temp.next
        